from selenium import webdriver

import time  
   
from selenium.webdriver.common.keys import Keys  

browser = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
browser.get('https://piraiinfo.com') 
  

time.sleep(2) 
   
login = browser.find_elements_by_xpath('//*[@id="menu-item-28"]/a') 
print(login)

login[0].click() 
  
print("About us")
login = browser.find_elements_by_xpath('//*[@id="menu-item-637"]/a') 
print(login)

login[0].click() 
  
print("services") 
login = browser.find_elements_by_xpath('//*[@id="menu-item-643"]/a') 
print(login)
 
login[0].click() 
  
print("data services") 

login = browser.find_elements_by_xpath('//*[@id="menu-item-637"]/a') 
print(login)

login[0].click() 
  
print("services") 
login = browser.find_elements_by_xpath('//*[@id="menu-item-636"]/a') 
print(login)

login[0].click() 
  
print("cloud services")

login = browser.find_elements_by_xpath('//*[@id="menu-item-637"]/a') 
print(login)

login[0].click() 
  
print("services") 
login = browser.find_elements_by_xpath('//*[@id="menu-item-702"]/a') 
print(login)

login[0].click() 
  
print("devops services")

login = browser.find_elements_by_xpath('//*[@id="menu-item-30"]/a') 
print(login)
 
login[0].click() 
  
print("contact us")
user = browser.find_elements_by_xpath('//*[@id="wpcf7-f270-p23-o1"]/form/p[1]/span/input') 
  

user[0].send_keys('preethica')
user = browser.find_elements_by_xpath('//*[@id="wpcf7-f270-p23-o1"]/form/p[2]/span/input') 
  

user[0].send_keys('preethicca1999@gmail.com') 
user = browser.find_elements_by_xpath('//*[@id="wpcf7-f270-p23-o1"]/form/p[3]/span/input') 
  

user[0].send_keys('9345670075')

user = browser.find_elements_by_xpath('//*[@id="wpcf7-f270-p23-o1"]/form/p[4]/span/textarea') 

user[0].send_keys('test') 
  
login = browser.find_elements_by_xpath('//*[@id="wpcf7-f270-p23-o1"]/form/p[5]/input') 
print(login)

login[0].click() 
  
print("submit")

browser.close()  
