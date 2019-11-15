from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

box=browser.find_element_by_tag_name("img")
x=box.get_attribute("valuex")
print(x)
y=calc(x)
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
element=browser.find_element_by_id("robotCheckbox")
element.click()
element1=browser.find_element_by_id("robotsRule")
element1.click()
button=browser.find_element_by_class_name("btn.btn-default")
button.click()
