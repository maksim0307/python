from selenium import webdriver

driver = webdriver.Firefox(executable_path="geckodriver.exe")

url = "https://www.facebook.com/campaign/landing.php?campaign_id=298364580528938&extra_1=yandex_15925352376%7Cdesktop%7C1903759853%7C%7C%D1%84%D0%B0%D1%86%D0%B5%D0%B1%D0%BE%D0%BE%D0%BA%7Cnone%7C8095dy448850&placement=none&creative=1903759853&keyword=%D1%84%D0%B0%D1%86%D0%B5%D0%B1%D0%BE%D0%BE%D0%BA&partner_id=yandexsem&extra_2=search&adposition=premium_1&yclid=13522746797539459071"
driver.maximize_window()
driver.get(url)

a = driver.find_element_by_class_name("_9bq5").click()

email_input = driver.find_element_by_id("email")
pass_input = driver.find_element_by_id("pass")
button_login = driver.find_element_by_id("loginbutton")

email_input.send_keys("Логин Васяна")
pass_input.send_keys("Пароль 12345")
button_login.click()
