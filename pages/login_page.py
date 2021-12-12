from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_url_contain('login'), "Url is not correct"

    def should_be_login_form(self):
        assert (self.is_element_present(*LoginPageLocators.LOGIN_FIELD)
                and self.is_element_present(*LoginPageLocators.PASSWORD_FIELD)
                and self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT)), "No login form"

    def should_be_register_form(self):
        assert (self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL)
                and self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1)
                and self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2)
                and self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT)), "No registration form"
