import pytest
from utils.constants import *
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in Your Browser Name e.g chrome, Firefox")

@pytest.fixture (scope = 'class')
def test_launch_browser(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/SRIHARI/Downloads/drivers/chromedriver.exe")
    elif browser == "ff":
        driver = webdriver.Firefox(executable_path="C:/Users/SRIHARI/Downloads/drivers/geckodriver.exe")
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.quit()
