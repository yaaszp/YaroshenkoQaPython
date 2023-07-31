from modules.ui.page_objects.Rozetka.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class LogInPage(HomePage):
    EMAIL_INPUT_FIELD = "//*[@id='auth_email']"
    PASSWORD_INPUT_FIELD = "//*[@id='auth_pass']"
    ENTER_BUTTON = (
        "//rz-single-modal-window//rz-auth//form/fieldset//button[text()=' Увійти ']"
    )
    REGISTRATION_BUTTON = "//rz-single-modal-window//rz-auth//form/fieldset//button[text()=' Зареєструватися ']"
    REMEMBER_ME_CHECKBOX = "//*[@id='remember_me']"
    WARNING_MESSAGE = "//rz-single-modal-window//rz-user-identification/rz-auth/div/form/fieldset//strong[text()=' Введено невірний пароль! ']"

    def __init__(self) -> None:
        super().__init__()

    def enter_email(self, email):
        self.driver.implicitly_wait(10)
        email_field = self.driver.find_element(By.XPATH, self.EMAIL_INPUT_FIELD)
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.XPATH, self.PASSWORD_INPUT_FIELD)
        password_field.send_keys(password)

    def click_remember_me_checkbox(self):
        remember_me_checkbox = self.driver.find_element(
            By.XPATH, self.REMEMBER_ME_CHECKBOX
        )
        remember_me_checkbox.click()

    def click_enter_button(self):
        enter_button = self.driver.find_element(By.XPATH, self.ENTER_BUTTON)
        enter_button.click()
        self.driver.implicitly_wait(5)
