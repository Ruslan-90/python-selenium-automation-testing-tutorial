import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_basket_button_exists(browser):
    browser.get(link)
    time.sleep(5)
    add_basket = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert add_basket.is_displayed() == True
