import webdriver_manager.chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest


@pytest.fixture
def setup():
    global mname,yof,dirname,distname,proname,driver
    mname = input("Enter the name")
    yof = input("Enter the year")
    dirname = ("Enter the dirname")
    distname = ("Enter the distname")
    proname = ("Enter proname")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close
def test_movie(setup):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(mname)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(yof)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(distname)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(distname)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(proname)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[4]").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(1)



