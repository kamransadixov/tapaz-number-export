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
import datetime

# Paste url
url = "URL GOES HERE"

# Generate random number for sleep time
for index in range(1):
	randomnumber = (random.randint(1, 3))

# Define browser
browser = webdriver.Firefox()

# Set windows size
browser.set_window_size(1100, 900)
browser.get(url)
time.sleep(randomnumber)
print(datetime.datetime.now())

# Start HTML file part 1
print('<!doctype html>')
print('<html lang="en">')
print('	<head>')
print('		<!-- Required meta tags -->')
print('		<meta charset="utf-8">')
print('		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">')
print('		<!-- Bootstrap CSS -->')
print('		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">')
print('		<title>Hello, world!</title>')
print('	</head>')
print('	<body>')
# End HTML file part 1

# Ads link scaner
for divnumber in range(1, 10000):
	try:
		post = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[3]/div['+ str(divnumber) +']/a')
		postlink = post.get_attribute('href')
		postname_xpath = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[3]/div[3]/div['+ str(divnumber) +']/a/div[2]')#964
		postname = postname_xpath.get_attribute('innerHTML')
		print(str(divnumber) + '		<a href="' + str(postlink) + '" class="' + str(postname) + '">' + str(divnumber) + '</a></br>')
	except NoSuchElementException:
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)

# Start HTML file part 2
print('		<!-- Optional JavaScript -->')
print('		<!-- jQuery first, then Popper.js, then Bootstrap JS -->')
print('		<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>')
print('		<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>')
print('		<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>')
print('	</body>')
print('</html>')
# End HTML file part 2

print(datetime.datetime.now())