import requests
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
response = requests.get("https://www.uniprot.org/docs/pkinfam")
soup = bs(response.text,"lxml")
links = soup.findAll('a')
links = links[39:1066]
kinase_list = []
label = ["kinase"]
for i in links:
    kinase_list.append(i.text)
df = pd.DataFrame(kinase_list,columns = label)

path_to_driver = "/Users/athreya/Downloads/chromedriver"
driver = webdriver.Chrome(path_to_driver)