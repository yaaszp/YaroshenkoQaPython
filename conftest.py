import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database


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
    db = Database()
    yield db
