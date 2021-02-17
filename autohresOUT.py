from selenium import webdriver
import time
import credential

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# print(driver.title)
driver.get("https://10.50.15.213/#/login")
driver.set_page_load_timeout(45)
driver.maximize_window()
driver.implicitly_wait(10)
advButton = driver.find_element_by_xpath('/html/body/div/div[2]/button[3]')
advButton.click()
contButton = driver.find_element_by_xpath('//*[@id="proceed-link"]')
contButton.click()
eeID = driver.find_element_by_xpath('//*[@id="login"]/div/main/div/div/div/div/div/div[1]/form/div[2]/div/div[1]/div[1]/input')
eeID.send_keys(credential.username_hres)
eePW = driver.find_element_by_xpath('//*[@id="login"]/div/main/div/div/div/div/div/div[1]/form/div[3]/div/div[1]/div[1]/input')
eePW.send_keys(credential.password)
loginButton = driver.find_element_by_xpath('//*[@id="login"]/div/main/div/div/div/div/div/div[2]/button[2]/div')
loginButton.click()
timeoutButton = driver.find_element_by_xpath('//*[@id="inspire"]/div[2]/main/div/div[2]/div/div/div[2]/div/div/div[1]/button[2]')
timeoutButton.click()
sortDate = driver.find_element_by_xpath('//*[@id="inspire"]/div[2]/main/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/table/thead/tr[1]/th[1]')
sortDate.click()
time.sleep(1)
timeIN = driver.find_element_by_xpath('//*[@id="inspire"]/div[2]/main/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[3]').text

import pymsgbox
pymsgbox.alert('Timed-out @ ' + timeIN, 'HRES', 'OK')