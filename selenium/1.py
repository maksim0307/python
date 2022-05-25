from selenium import webdriver
driver = webdriver.Firefox(executable_path="geckodriver.exe")
driver.maximize_window()
url = "https://yandex.ru/"
url1 = """ //*[@id="text"] """
driver.get(url)
search = driver.find_element_by_xpath("url1")
search.send_keys("M5")
search.submit()
























