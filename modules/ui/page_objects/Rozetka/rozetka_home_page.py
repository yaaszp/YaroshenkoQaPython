from modules.ui.page_objects.Rozetka.rozetka_base_page import BasePage
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from modules.ui.page_objects.Rozetka.rozetka_log_in_page import LogInPage


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

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def go_to(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def enter_search_query(self, query):
        search_field = self.driver.find_element(By.XPATH, self.SEARCH_INPUT_FIELD)
        search_field.send_keys(query + Keys.ENTER)

    def click_log_in_button(self):
        # self.ex_waiter(By.XPATH, self.LOG_IN_BUTTON)
        # self.implicitly_waiter(30)
        log_in_button = self.driver.find_element(By.XPATH, self.LOG_IN_BUTTON)
        log_in_button.click()

    def click_cart_button(self):
        self.driver.implicitly_wait(5)
        cart_button = self.driver.find_element(By.XPATH, self.CART_BUTTON)
        cart_button.click()

    def header_is_visible(self):
        return self.driver.find_element(By.XPATH, self.HEADER).is_displayed()

    def sidebar_is_visible(self):
        return self.driver.find_element(By.XPATH, self.SIDEBAR).is_displayed()

    def main_content_is_visible(self):
        return self.driver.find_element(By.XPATH, self.MAIN_CONTENT).is_displayed()

    def log_in_window_is_visible(self):
        return self.driver.find_element(By.XPATH, self.LOG_IN_WINDOW).is_displayed()

    def cart_window_is_visible(self):
        return self.driver.find_element(By.XPATH, self.CART_WINDOW).is_displayed()

    def get_current_url(self):
        return self.driver.current_url

    def get_text_from_url(self, txt):
        current_url = self.driver.current_url
        return current_url.count(txt)

    def go_to_login_page(self):
        login_page = LogInPage(self.driver)
        login_page.go_to()
        return login_page
