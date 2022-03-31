import webdriver_manager.chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


@pytest.fixture
def setup():
    global name,driver
    name = input("Enter the name")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(7)
    driver.close()


def test_form(setup):
    driver.get("https://iprimedtraining.herokuapp.com/")
    driver.find_element_by_name("name").send_keys(name)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[4]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[4]/td[2]/div/input").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(5)
