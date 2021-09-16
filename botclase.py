from selenium import webdriver
import time

browser=webdriver.Edge(executable_path='./driver/msedgedriver')

def botwhatsapp():
    browser.get("https://web.whatsapp.com")
    time.sleep(5)


botwhatsapp()