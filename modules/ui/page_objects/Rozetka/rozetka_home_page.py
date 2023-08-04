from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from modules.ui.page_objects.Rozetka.rozetka_base_page import BasePage
from modules.ui.page_objects.Rozetka.rozetka_search_page import SearchPage


class HomePage(BasePage):
    URL = "https://rozetka.com.ua/"
    SEARCH_INPUT_FIELD = "//rz-main-header/header//input[@name = 'search']"
    LOG_IN_BUTTON = "//rz-header/rz-main-header/header//rz-user/button"
    CART_BUTTON = "//rz-header/rz-main-header/header//rz-cart/button"
    LOG_IN_WINDOW = "//rz-single-modal-window"
    CART_WINDOW = "//rz-single-modal-window"
    HEADER = "//rz-header"
    SIDEBAR = "//rz-main-page//aside/rz-main-page-sidebar"
    MAIN_CONTENT = "//rz-main-page//main"

    EMAIL_INPUT_FIELD = "//*[@id='auth_email']"
    PASSWORD_INPUT_FIELD = "//*[@id='auth_pass']"
    REMEMBER_ME_CHECKBOX = "//rz-single-modal-window//rz-user-identification/rz-auth//form/fieldset/div[3]/label"
    ENTER_BUTTON = (
        "//rz-single-modal-window//rz-auth//form/fieldset//button[text()=' Увійти ']"
    )
    ERROR_MESSAGE = "//rz-single-modal-window//rz-user-identification/rz-auth/div/form/fieldset//rz-re-captcha//p"

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def go_to(self):
        self.driver.get(self.URL)

    def enter_search_query(self, query):
        search_field = self.driver.find_element(By.XPATH, self.SEARCH_INPUT_FIELD)
        search_field.send_keys(query + Keys.ENTER)

    def click_log_in_button(self):
        log_in_button = self.driver.find_element(By.XPATH, self.LOG_IN_BUTTON)
        log_in_button.click()

    def click_cart_button(self):
        cart_button = self.driver.find_element(By.XPATH, self.CART_BUTTON)
        cart_button.click()

    def header_is_visible(self):
        return self.driver.find_element(By.XPATH, self.HEADER).is_displayed()

    def sidebar_is_visible(self):
        return self.driver.find_element(By.XPATH, self.SIDEBAR).is_displayed()

    def main_content_is_visible(self):
        return self.driver.find_element(By.XPATH, self.MAIN_CONTENT).is_displayed()

    def log_in_window_is_visible(self):
        log_in_window = self.waite_element_by_locator(self.LOG_IN_WINDOW)
        return log_in_window.is_displayed()

    def cart_window_is_visible(self):
        cart_window = self.waite_element_by_locator(self.CART_WINDOW)
        return cart_window.is_displayed()

    def get_current_url(self):
        return self.driver.current_url

    def get_text_from_url(self, txt):
        current_url = self.driver.current_url
        return current_url.count(txt)

    def enter_email(self, email):
        email_field = self.waite_element_by_locator(self.EMAIL_INPUT_FIELD)
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.waite_element_by_locator(self.PASSWORD_INPUT_FIELD)
        password_field.send_keys(password)

    def click_remember_me_checkbox(self):
        remember_me_checkbox = self.waite_element_by_locator(self.REMEMBER_ME_CHECKBOX)
        remember_me_checkbox.click()

    def click_enter_button(self):
        enter_button = self.waite_element_by_locator(self.ENTER_BUTTON)
        enter_button.click()

    def get_error_message(self):
        error_message = self.waite_element_by_locator(self.ERROR_MESSAGE)
        return error_message.text

    def go_to_search_page(self):
        search_page = SearchPage(self.driver)
        return search_page
