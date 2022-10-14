from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
chromeOptions = webdriver.ChromeOptions()
import sqlite3
connection = sqlite3.connect("D:\database_new\gcoos_data_v3.sqlite")
crsr = connection.cursor()
prefs = {'safebrowsing.enabled': 'false',
'download.default_directory' : 'D:\map_images\Platforms'}
chromeOptions.add_experimental_option("prefs", prefs)
chromeOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
driverService = Service('D:/GRIIDC_Automation-main/GRIIDC_Automation-main/chromedriver.exe') 
driver = webdriver.Chrome(service=driverService,options=chromeOptions)
for i in range(1,60):
    y = str(i)
    crsr.execute('''select p.rowid from platform p join organization o on p.orgId =  o.rowId where o.rowId =?;''', (i,))
    ans = crsr.fetchall()
    print('total platforms=',len(ans))
    for j in ans:
        x = str(j[0])
        driver.get('http://localhost/map_images/mapCP_NTL2.php?org='+y+'&plat='+x+'&make=1')
        # driver.implicitly_wait(5000)
        time.sleep(2)
        btn_ok = driver.find_element(By.ID, "save-image-btn").click()
time.sleep(3000)
connection.close()
driver.close()