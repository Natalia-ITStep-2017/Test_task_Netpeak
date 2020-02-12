import random
import time
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver: WebDriver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)

   #1. Перейти по ссылке на главную страницу сайта Netpeak. (https://netpeak.ua/)
driver.get("https://netpeak.ua")
url_home_page = driver.current_url

   #2. Перейдите на страницу "Работа в Netpeak", нажав на кнопку "Карьера"
driver.find_element_by_xpath('//nav[@id="main-menu"]//li[@class="blog"]').click()

   #3. Перейти на страницу заполнения анкеты, нажав кнопку - "Я хочу работать в Netpeak"
driver.find_element_by_xpath('//a[@class="btn green-btn"]').click()


   #4. Загрузить файл с недопустимым форматом в блоке "Резюме", например png,
   # и проверить что на странице появилось сообщение, о том что формат изображения неверный.
driver.find_element_by_xpath("//input[@type='file']").send_keys("D:\cv.jpg")
wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="up_file_name"]/label')))
time.sleep (5)
assert 'неверный формат файла' in driver.find_element_by_xpath('//div[@id="up_file_name"]/label').text

   #5. Заполнить случайными данными блок "3. Личные данные"
first_name = ['Vasya', 'Yura', 'Andrey', 'Dima']
last_name=['Petrenko', 'Teprenko', 'Reptenko', 'Netrepko']
el_ad = ['user1@example.com', 'user2@example.com', 'user3@example.com', 'user4@example.com']
driver.find_element_by_name('name').send_keys(random.choice(first_name))
driver.find_element_by_name('lastname').send_keys(random.choice(last_name))
driver.find_element_by_name('hiringe').send_keys(random.choice(el_ad))
Select(driver.find_element_by_name('bd')).select_by_index(random.randint(0, 30))
Select(driver.find_element_by_name('bm')).select_by_index(random.randint(0, 11))
Select(driver.find_element_by_name('by')).select_by_index(random.randint(0, 59))
driver.find_element_by_name('phone').click()
driver.find_element_by_name('phone').send_keys('0' + str(random.randint(100000000, 999999999)))

   #6. Нажать на кнопку отправить резюме
driver.find_element_by_xpath('//button[@id="submit"]').click()

   #7. Проверить что сообщение на текущей странице  - "Все поля являются обязательными для заполнения" -
   # подсветилось красным цветом
assert driver.find_element(By.XPATH, '//p[@class="warning-fields help-block"]')\
           .value_of_css_property('color') == 'rgb(255, 0, 0)'

   #8. Нажать на логотип для перехода на главную страницу и убедиться что открылась нужная страница.
driver.find_element_by_xpath('//div[@class="logo-block"]/a/img').click()
time.sleep (5)
assert driver.current_url == url_home_page

driver.close()


