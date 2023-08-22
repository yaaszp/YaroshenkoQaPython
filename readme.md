This is an educational project. This project contains UI tests, API tests, and DB tests. 
The project has a base frame structure
For UI tests was used page object model.
For API tests was created base API client.

The test framework has the next base structure:

config – this folder is for different configurations

modules – this folder contains additional useful files, API clients, Objects of pages, SQL queries for Database and the other useful classes 

tests – this folder contains tests

pytest.py – this file contains marks for tests and descriptions for these marks

conftest.py – this file contains fixtures for tests

chromedriver.exe – driver for Chrome browser

become_qa_auto.db – sample database file

.gitignore – file for GitHub

readme.md – information file

The API tests was written for open GitHub API interface
https://docs.github.com/en/rest?apiVersion=2022-11-28

For API tests was created API client. It is the file “github.py”. The file contains requests to the API interface GitHub.
The folder “tests/API” contains the file “test_github_api.py”
The file contains tests for the API interface.
For starting API tests are used fixture “github_api” from file “conftest.py”

For UI tests was used Page Object model.
For testing used Web site Rozetka
https://rozetka.com.ua/ua/
Folder “modules/ui/page objects/Rozetka” contains objects of pages
Folder “tests/ui” contains file “test_ui_rozetka.py”
The file contains tests for the UI interface.

For DataBase tests was created file “database.py” that contains SQL queries to Data Base. The file is used “SQLite” library
File “General.py” contains a class with static methods. These methods work with strings. The folder “tests/database” contains tests for Data Base
	

In order to start tests you need to execute command:
pytest -m your_marks

For example, in order to start API tests you need to execute command:
pytest -m api_apiadditional

In order to start UI tests for Rozetka you need to execute command:
pytest -m ui_additional

In order to start DataBase tests you need to execute command:
pytest -m database_additional
pytest -m database_additional_negative


All these tests executed successfully :)

