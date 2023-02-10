from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

opt = webdriver.ChromeOptions()
opt.add_argument('headless')
driver = webdriver.Chrome(service=Service(r"C:\chromedriver_win32\chromedriver.exe"), options=opt)



driver.get('https://www.worldometers.info/world-population/#top20')
time.sleep(10)
chi = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[1]/div/div[2]/div[1]/div[1]/span[4]/span')
print(chi.text)