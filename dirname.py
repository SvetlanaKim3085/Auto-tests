from selenium import webdriver
import os
import time 

link="http://suninjuly.github.io/file_input.html"
browser=webdriver.Chrome()
browser.get(link)

first=browser.find_element_by_name("firstname")
first.send_keys("KIm")
last=browser.find_element_by_name("lastname")
last.send_keys("Km")
email=browser.find_element_by_name("email")
email.send_keys("sdsdffs")
input1=browser.find_element_by_name("file")
current_dir = os.path.abspath(os.path.dirname(__file__))    
file_path = os.path.join(current_dir, 'new_6.txt')           
input1.send_keys(file_path)
button=browser.find_element_by_class_name("btn.btn-primary")
button.click()