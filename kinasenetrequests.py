import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
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
actions = ActionChains(driver)

url = "http://www.kinasenet.ca/showProtein"
#411 379 are the x and y of the first query
#389,400 are the xy of the second one
#according to my calculations - each box is 22
query = "a"
xpos = 411
ypos = 440
driver.get(url)
sbox = driver.find_element_by_name("query")
sbox.send_keys(query)
pyautogui.moveTo(xpos, ypos)
time.sleep(1.5)
pyautogui.click()
submit_button = driver.find_element_by_id("search").click()