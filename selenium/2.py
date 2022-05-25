import time
from selenium import webdriver
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.get("https://vk.com/")
time.sleep(6)
login = driver.find_element_by_id("index_email")
password = driver.find_element_by_id("index_pass")
button = driver.find_element_by_id("index_login_button")
login.send_keys("AMOGUS666")
time.sleep(2)
password.send_keys("пароль")
time.sleep(1)
button.click()
a = "/html/body/div[7]/div/div[2]/div/div[2]/div/div[2]/input"
b = driver.find_element_by_xpath(a)



