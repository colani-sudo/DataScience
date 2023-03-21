#Web Crawling HW5               
#Created by Matsenjwa Colani        410921343
#Imports
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1st Part
url = 'https://sys.ndhu.edu.tw/SA/XSL_ApplyRWD/ActApply.aspx?lang=en'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser').text      #can also use lmxl parser

print(soup)