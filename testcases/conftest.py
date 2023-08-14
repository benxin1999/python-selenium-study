import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://meikefresh.5istudy.online/')
    yield driver
    driver.quit()
