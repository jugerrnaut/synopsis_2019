from selenium import webdriver
import pandas as pd
import csv
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import joblib
import numpy as np
df = pd.read_csv("kinases.csv")
def getInhibitors(kinasedf,column,path_to_driver = "/Users/athreya/Downloads/chromedriver",url = "http://www.kinasenet.ca/showProtein"):
    driver = webdriver.Chrome(path_to_driver)
    try:
        for i in kinasedf["{}".format(column)]: 
            driver.get(url)
            sbox = driver.find_element_by_name("query")
            sbox.send_keys(i)
            submit_button = driver.find_element_by_id("search").click()
            results = driver.find_elements_by_class_name("name")
            inhibitorList = []
            for i in results:
                inhibitorList.append([i,i.text])
        print(inhibitorList)
        joblib.dump(np.array(inhibitorList),"myinhibitors.npy")
    except:
        print(inhibitorList)
        joblib.dump(np.array(inhibitorList),"myinhibitors.npy")
getInhibitors(df, "Short Name")
