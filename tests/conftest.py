import pytest as pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver_fixture():
    pytest.driver = webdriver.Chrome('../WebDriver/chromedriver.exe ')
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield
    pytest.driver.quit()
