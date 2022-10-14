from selenium import webdriver 
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
chromeOptions = webdriver.ChromeOptions()
prefs = {'safebrowsing.enabled': 'false',
'download.default_directory' : 'D:\map_images\plat_new'}
chromeOptions.add_experimental_option("prefs", prefs)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
driverService = Service('D:/GRIIDC_Automation-main/GRIIDC_Automation-main/chromedriver.exe') 
driver = webdriver.Chrome(service=driverService,options=chromeOptions)
for i in range(1,60):
    y = str(i)
    driver.get('http://localhost/map_images/mapCP_NTL2.php?org='+y+'&make=0')
        # driver.implicitly_wait(5000)
    time.sleep(2)
    btn_ok = driver.find_element(By.ID, "save-image-btn").click()
time.sleep(3000)
driver.close()