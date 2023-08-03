from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver.implicitly_wait(10)

    def close(self):
        self.driver.close()

    def wait_for_visibility_of_element_located(self, locator, locator_value):
        wait = WebDriverWait(self.driver, timeout=10)

        element = wait.until(EC.visibility_of_element_located((locator, locator_value)))
        if element is False:
            raise Exception(f"No element found by {locator_value}")
        return element

    def implicitly_waiter(self, timeout):
        self.driver.implicitly_wait(timeout)
