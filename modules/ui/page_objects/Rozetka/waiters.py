from modules.ui.page_objects.Rozetka.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Waiters(BasePage):
    def __init__(self) -> None:
        super().__init__()

    def ex_waiter(self, locator):
        wait = WebDriverWait(self.driver, timeout=10)
        el = wait.until(EC.visibility_of(locator))

    def imp_waiter(self, timeout):
        self.driver.implicitly_wait(timeout)
