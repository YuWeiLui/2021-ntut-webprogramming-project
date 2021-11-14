#this is the beggining of main.py
import requests
from bs4 import BeautifulSoup 
import pandas as pd

html = requests.get("https://mbasic.facebook.com/")
bsObj = BeautifulSoup(html.content, "lxml") 
print(bsObj) #This is login webpage, need password, please write login code next line
#this is the end of main.py