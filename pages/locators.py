from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FIELD = (By.ID, "id_login-username")
    PASSWORD_FIELD = (By.ID, "id_login-password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "[name='login_submit']")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")
