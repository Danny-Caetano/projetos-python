import time

from selenium import webdriver

from chrome.service import Service

service = Service('/path/to/chromedriver')

service.start()

driver = webdriver.Remote(service.service_url)

driver.get('http://www.google.com/')

time.sleep(5) # Let the user actually see something!

driver.quit()