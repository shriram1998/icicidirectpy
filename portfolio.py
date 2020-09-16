#This program will take screenshot of your portfolio and store it to cwd
import os,time
from selenium import webdriver
from datetime import datetime
from datetime import timedelta
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))
chromedriver = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver.exe')
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

#Enter username, password and dob here
username=""
password=""
dob=""
driver.get('https://secure.icicidirect.com/IDirectTrading/customer/login.aspx')
driver.find_element_by_xpath('//input[@id="txtUserId"]').send_keys(username)
driver.find_element_by_xpath('//input[@id="txtPass"]').send_keys(password)
driver.find_element_by_xpath('//input[@id="txtDOB"]').send_keys(dob)
driver.find_element_by_xpath('//input[@id="Button1"]').click()
driver.minimize_window()
time.sleep(1)

#Open Portfolio Page
driver.find_element_by_xpath('//*[@id="pnlmnudsp"]/div[1]/div/ul/li[1]/a').click()
time.sleep(1)

#Save portfolio
portfolio = driver.find_element_by_xpath('//*[@id="equity"]/div[3]/div/div[1]').screenshot_as_png
filename =os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Portfolio on '+str(datetime.today().date())+'.png')
driver.get("https://secure.icicidirect.com/customer/logout")
driver.quit()
with open(filename, "wb") as file:
  file.write(portfolio)

#To remove previous day's image
oldPath=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Portfolio on '+str((datetime.today()-timedelta(days=1)).date())+'.png')
if os.path.exists(oldPath):
  os.remove(oldPath)
else:
  pass

#To open the image and display it
try:
    img = Image.open(portfolioPath)
    img.show()
except Exception as e:
    print("Issue opening image: ",e)
