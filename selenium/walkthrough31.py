# #!/usr/bin/env python
from selenium import webdriver


# Start the browser and navigate to http://automationpractice.com/index.php.
driver = webdriver.Chrome()
driver.get('http://automationpractice.com/index.php')
driver.find_element_by_css_selector("input[id='search_query_topcd']").send_keys("dresses")
#driver.find_element_by_css_selector("input[id ='order']")