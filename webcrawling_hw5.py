# Web Crawling HW5               
# Created by Matsenjwa Colani        410921343

#import libraries
    
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://sys.ndhu.edu.tw/SA/XSL_ApplyRWD/ActApply.aspx'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')     #can also use lmxl parser

for x in range(10):
    id_ = 'BodyContent_gvActs_lblGv_act_name_' + str(x)
    activities = soup.find('span', id=id_)
    print(activities.contents)
    
column_headers = ['Name of the Activity',
                  'Number of Certified Hours',
                   'Number of people who have registered',
                   'Date and time of registration',
                   'Date and Time of the activity']
dataframe = pd.DataFrame(columns = column_headers)

activityname=''
certhours=''
enrolled=''
regtime=''
activityhours=''

for tr in range(10):
    # print(activities.contents)
    id_ = 'BodyContent_gvActs_lblGv_act_name_' + str(tr)
    activityname = soup.find('span', id=id_).contents
    id_ = 'BodyContent_gvActs_lblGv_xsl_check_' + str(tr)
    certhours = soup.find('span', id=id_).contents
    id_ = 'BodyContent_gvActs_lblGv_reg_num_' + str(tr)
    enrolled = soup.find('span', id=id_).contents
    id_ = 'BodyContent_gvActs_lblGv_reg_dt_' + str(tr)
    regtime = soup.find('span', id=id_).contents
    id_ = 'BodyContent_gvActs_lblGv_xsl_check_' + str(tr)    
    activityhours = soup.find('span', id=id_).contents
    
    if (activityname != ''):
         dataframe = dataframe.append(
            pd.Series([
            activityname,
            certhours,
            enrolled,
            regtime,
            activityhours
            ],
            index = column_headers),
            ignore_index = True)
            
dataframe.sort_values("%Change", axis = 0, ascending = False,
                      inplace = True, na_position = 'last')
                      
print(dataframe)


