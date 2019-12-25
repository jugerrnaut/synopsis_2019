from biopandas.pdb import PandasPdb
import pandas as pd
import pyautogui
import selenium
from pypdb import *
import time
from selenium import webdriver
import joblib
import numpy as np
path_to_driver = "/Users/athreya/Downloads/chromedriver"
driver = webdriver.Chrome(path_to_driver)
df = pd.read_csv("kinases.csv")
id_list = []
counter = 0
#eleven requests is the max at one time
try:
    for i in df["Short Name"]:
        print(counter)
        if counter%10 == 0 and counter!=0:
            time.sleep(30)
        else:
            query = "{}".format(i)
            driver.get("https://www.rcsb.org/")
            sbox = driver.find_element_by_name("q")
            sbox.send_keys(query)
            time.sleep(2)
            submit_button = driver.find_element_by_id("searchbutton").click()
            time.sleep(2)
            pyautogui.moveTo(575, 714)
            time.sleep(2) 
            pyautogui.click()
            time.sleep(2)
            id_list.append(driver.find_element_by_id("structureID").text)
        counter+=1
except:
    joblib.dump(np.array(id_list),'pdbids.npy')
driver.quit()
print(id_list)
joblib.dump(np.array(id_list),'pdbids.npy')