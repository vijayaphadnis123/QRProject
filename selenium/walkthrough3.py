# #!/usr/bin/env python
from selenium import webdriver


# Start the browser and navigate to http://automationpractice.com/index.php.
driver = webdriver.Chrome()
url = 'http://automationpractice.com/index.php'
search_item = "dress"
driver.get(url)
print ('Navigating to ' + url)
driver.find_element_by_css_selector("input[id='search_query_top']").send_keys(search_item)
print ('Searching for ' + search_item)
#driver.find_element_by_css_selector("input[id ='order']")
driver.find_element_by_css_selector("button[class='btn btn-default button-search']").click()