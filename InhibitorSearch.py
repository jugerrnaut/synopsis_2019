from selenium import webdriver
import pandas as pd
import csv
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import joblib
import numpy as np
df = pd.read_csv("kinases.csv")
path_to_driver = "/Users/athreya/Downloads/chromedriver"
driver = webdriver.Chrome(path_to_driver)
url = "http://www.kinasenet.ca/showProtein"
inhibitorList = []
def getinhibitors():
    try:
        for i in df["{}".format("Short Name")]: 
            driver.get(url)
            sbox = driver.find_element_by_name("query")
            sbox.send_keys(i)
            submit_button = driver.find_element_by_id("search").click()
            results = driver.find_elements_by_class_name("name")
            for n in results:
                inhibitorList.append([i,n.text])
        print(inhibitorList)
        joblib.dump(inhibitorList,"myinhibitors.npy")
    except:
        print(inhibitorList)
        joblib.dump(inhibitorList,"myinhibitors.npy")
    driver.quit()
#getinhibitors()
