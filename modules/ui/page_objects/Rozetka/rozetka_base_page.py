from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def close(self):
        self.driver.close()

    def waite_element_by_locator(self, locator):
        wait = WebDriverWait(self.driver, timeout=15)
        element = wait.until(lambda d: d.find_element(By.XPATH, locator))
        return element
