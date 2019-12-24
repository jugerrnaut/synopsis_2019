from selenium import webdriver
import pandas as pd
import csv
from bs4 import BeautifulSoup as bs
import requests

def getInhibitors(kinase):
    path_to_driver = "/Users/23gordonc/Downloads/chromedriver"
    driver = webdriver.Chrome(path_to_driver)
    url = "http://www.kinasenet.ca/showProtein"
    query = kinase
    driver.get(url)
    sbox = driver.find_element_by_name("query")
    sbox.send_keys(query)
    submit_button = driver.find_element_by_id("search").click()
    results = driver.find_elements_by_class_name("name")
    inhibitorList = []
    for i in results:
        inhibitorList.append(i.text)
        return inhibitorList
