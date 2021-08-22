from selenium import webdriver
import math, time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id('num1').text)
    y = int(browser.find_element_by_id('num2').text)
    z = x + y

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(z))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()