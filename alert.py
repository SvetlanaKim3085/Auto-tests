from selenium import webdriver
import math

browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

button=browser.find_element_by_class_name("btn.btn-primary")
button.click()
confirm=browser.switch_to.alert
confirm.accept()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
element=browser.find_element_by_id("input_value")
x=element.text
y=calc(x)

input=browser.find_element_by_id("answer")
input.send_keys(y)

submit=browser.find_element_by_class_name("btn.btn-primary")
submit.click()

    
