from selenium import webdriver
import re

# Creating Firefox Driver instance/object
driver = webdriver.Firefox()
driver.get('http://www.airindia.in/contact-details.htm')

# Getting page source code in the form of a string
doc = driver.page_source

# Finding all the emails using regex filter
emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

for i in emails:
    print  i
