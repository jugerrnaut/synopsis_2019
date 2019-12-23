import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import bs4
from bs4 import BeautifulSoup as bs
import pandas as pd #for csv files
import random
import sklearn #some of the non nueral net machine learning stuff
import requests #making requests to the html
import json #lovely json
import pubchempy as pcp
from mpl_toolkits import mplot3d

#add in interactions between atoms

CID = [4133,2244]
  
columns = ["num atoms","coors", "bond coors","formal charge"]
test_df = pd.DataFrame(columns = columns)
bondslist = []
pointslookup = []
bondcoors = []
formal_charge = 0
elements = []
all_elements = []

def normalize(x):
     return (x + 2)/4

def createbondinglist(response):
    global bondslist
    leftbonds = response["aid1"]
    rightbonds = response["aid2"]
    bondtype = response["order"]
    for i in range(0,len(leftbonds)):
        bondslist.append([leftbonds[i],rightbonds[i],bondtype[i]])
    return bondslist

def create_data(CID):
    global test_df
    global bondslist
    global pointslookup
    global bondcoors
    global formal_charge
    global all_elements
    ax = plt.axes(projection='3d')
    for mol in CID:
        sample = pcp.Compound.from_cid('{}'.format(mol),record_type='3d')
        normal_sample = pcp.Compound.from_cid('{}'.format(mol))

        a = sample.record
        c = normal_sample.record
        
        atomic_info = sample.to_dict(properties=['atoms', 'bonds', 'inchi'])
        base = atomic_info["atoms"]
        for i in range(0,len(base)):
            elements.append(base[i]["element"])
        
        formal_charge = normal_sample.charge
        mapped_formal_charge = normalize(formal_charge)

        x_base = a["coords"][0]["conformers"][0]["x"]
        y_base = a["coords"][0]["conformers"][0]["y"]
        z_base = a["coords"][0]["conformers"][0]["z"]

        bonds = a["bonds"]

        for i in range(0,len(x_base)):
            markerstr = ""
            eoi = elements[i]
            if eoi =='C':
                markerstr = "x"
            elif eoi == "O":
                markerstr = "o"
            elif eoi == "N":
                markerstr = "v"
            elif eoi == "S":
                markerstr = "s"
            else:
                markerstr = "*"
            ax.plot([x_base[i]],[y_base[i]],[z_base[i]],marker=markerstr, markersize=10, color='black',alpha = mapped_formal_charge)
            pointslookup.append([[x_base[i]],[y_base[i]],[z_base[i]],eoi])

        createbondinglist(bonds)

        for n in range(0,len(pointslookup)):
            slpoint = bondslist[n][0]
            srpoint  = bondslist[n][1]
            color  = bondslist[n][2]

            colorstr = ""

            if color == 1:
                colorstr = "red"
            elif color == 2:
                colorstr = "blue"
            else:
                colorstr = "green"

            sl_point_x = pointslookup[slpoint-1][0][0]
            sl_point_y = pointslookup[slpoint-1][1][0]
            sl_point_z = pointslookup[slpoint-1][2][0]

            sr_point_x = pointslookup[srpoint-1][0][0]
            sr_point_y = pointslookup[srpoint-1][1][0]
            sr_point_z = pointslookup[srpoint-1][2][0]

            bondcoors.append([sl_point_x,sl_point_y,sl_point_z,sr_point_x,sr_point_y,sr_point_z])
            ax.plot((sl_point_x,sr_point_x),(sl_point_y,sr_point_y),(sl_point_z,sr_point_z),color = (colorstr))
        data = [[len(pointslookup),pointslookup,bondcoors,formal_charge]]
        df2 = pd.DataFrame(data,columns = columns)
        test_df = test_df.append(df2,ignore_index = True)
        print(test_df.head())
        data = []
        bondslist = []
        pointslookup = []
        bondcoors = []
        formal_charge = 0


create_data(CID)

plt.show()




