from selenium import webdriver
import math, time


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = str(browser.find_element_by_id('input_value').text)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x = calc(x)

    browser.find_element_by_css_selector("input[id='answer']").send_keys(x)

    browser.find_element_by_css_selector("input[id='robotCheckbox']").click()
    browser.find_element_by_css_selector("input[id='robotsRule']").click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()