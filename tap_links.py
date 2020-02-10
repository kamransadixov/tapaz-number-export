from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
import random
import sys
from selenium.webdriver.firefox.options import Options


for index in range(1):
	randomnumber = (random.randint(2, 3))
mainsite = '//file directory'
browser = webdriver.Firefox()
browser.set_window_size(1100, 900)

for divnumber in range(1, 101):
	browser.get(mainsite)
	post = browser.find_element_by_xpath('/html/body/a[' + str(divnumber) + ']')
	postlink = post.get_attribute('href')
	browser.get(postlink)
	
	#get phone number
	try:
		phonenumber_elem = browser.find_element_by_css_selector('.phone')
		phonenumber_link = phonenumber_elem.get_attribute('href')
		phonenumber_list = list(phonenumber_link)
		del phonenumber_list[0]
		del phonenumber_list[0]
		del phonenumber_list[0]
		del phonenumber_list[0]
		del phonenumber_list[0]
		del phonenumber_list[0]
		del phonenumber_list[2]
		del phonenumber_list[2]
		del phonenumber_list[5]
		del phonenumber_list[7]
		phonenumber = ''.join(phonenumber_list)

		username_elem = browser.find_element_by_css_selector('#js-lot-page > div.lot-body.l-center > div.aside-page.fixed-product-info > div.author > div.name')
		username = username_elem.get_attribute('innerHTML')
	except NoSuchElementException:
		pass

	print(divnumber, username, '   ', '+994' + phonenumber)

#python3 tap.py > text.txt