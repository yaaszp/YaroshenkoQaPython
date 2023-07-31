from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"D:\\python_basics\\Repo\\YaroshenkoQaPython"
    DRIVER_NAME = "chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()
