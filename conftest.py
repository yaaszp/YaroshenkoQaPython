import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from modules.ui.page_objects.Rozetka.rozetka_home_page import HomePage
from selenium.webdriver.chrome.options import Options


class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Oleksii"
        self.second_name = "Yaroshenko"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def db():
    database = Database()
    yield database


@pytest.fixture
def chrome_driver():
    path = r"D:\\python_basics\\Repo\\YaroshenkoQaPython"
    driver_name = "chromedriver.exe"
    options = Options()
    options.page_load_strategy = "normal"
    driver = webdriver.Chrome(options=options, service=Service(path + driver_name))
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def home_page(chrome_driver):
    page = HomePage(chrome_driver)

    yield page
    
    page.close()

    
