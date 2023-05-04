city_name = input()

# TODO: use title format for the city name
if city_name != 'all':
    city_name = city_name.title()

city_names = {
    "Keelung City": 2,
    "Taipei City": 3,
    "New Taipei City": 4,
    "Taoyuan City": 5,
    "Hsinchu City": 6,
    "Hsinchu County": 7,
    "Miaoli County": 8,
    "Taichung City": 9,
    "Changhua County": 10,
    "Nantou County": 11,
    "Yunlin County": 12,
    "Chiayi City": 13,
    "Chiayi County": 14,
    "Tainan City": 15,
    "Kaohsiung City": 16,
    "Pingtung County": 17,
    "Yilan County": 18,
    "Hualien County": 19,
    "Taitung County": 20,
    "Penghu County": 21,
    "Kinmen County": 22,
    "Lienchiang County": 23
}

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

driverPath = "chromedriver.exe"
s = Service(executable_path=driverPath)

browser = webdriver.Chrome(service=s)   
browser.get('https://www.cwb.gov.tw/V8/E/W/County/County.html?CID=63')  

browser.find_element(By.XPATH, '//*[@id="CID"]').click()

if city_name == 'all':
    for key,val in city_names.items():
        # browser.find_element(By.XPATH, '//*[@id="CID"]').click()
        sleep(1)
        browser.find_element(By.XPATH, f'//*[@id="CID"]/option[{val}]').click()
        temperature = browser.find_element(By.XPATH, '//*[@id="PC_Week_MOD"]/tbody/tr[1]/td[1]/p/span[1]').text
        
        print(f"{key}")
        print(f"{temperature}")
        
elif city_name in city_names:
    browser.find_element(By.XPATH, f'//*[@id="CID"]/option[{city_names[city_name]}]').click()
    temperature = browser.find_element(By.XPATH, '//*[@id="PC_Week_MOD"]/tbody/tr[1]/td[1]/p/span[1]').text
    print(f"{city_name}")
    print(f"{temperature}")
    
else:
    print("Not found.")

browser.quit()  