from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math


  
browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

num1=browser.find_element_by_id("num1")
num2=browser.find_element_by_id("num2")
x1=num1.text
x2=num2.text
y=str(int(x1)+ int(x2))

select=Select(browser.find_element_by_tag_name("select"))
select.select_by_value(y)

button=browser.find_element_by_tag_name("button")
button.click()