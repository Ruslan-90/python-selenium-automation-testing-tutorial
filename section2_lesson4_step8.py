from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book").click()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    answerField = browser.find_element_by_id('answer')
    answerField.send_keys(y)

    solve_button = browser.find_element_by_id("solve").click()

    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()

finally:
    # time.sleep(10)
    browser.quit()
