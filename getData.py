from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://leetcode.com/anuragsrawat/'

driver = webdriver.Safari()
driver.get(URL)

total = driver.find_element_by_xpath('//*[@id="profile-root"]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div[1]/div[2]')
print('Total Problems Solved: ', total.text)
