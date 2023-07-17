import logging
import time

import yaml
from testpage import OperationHelper

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)
login = testdata["login"]
passw = testdata["password"]


def test1(browser):
    logging.info("Start Test 1")
    testpage = OperationHelper()
    testpage.go_to_site()
    testpage.enter_login("Test")
    testpage.enter_password("Test")
    testpage.click_login_button()
    assert testpage.get_err_text() == "401"


def test2(browser):
    logging.info("Start Test 2")
    testpage = OperationHelper()
    testpage.go_to_site()
    testpage.enter_login(login)
    testpage.enter_password(passw)
    testpage.click_login_button()
    assert testpage.profile_text() == f"Hello, {login}"


def test3(browser):
    logging.info("Start Test 3")
    testpage = OperationHelper()
    testpage.go_to_site()
    testpage.enter_login(login)
    testpage.enter_password(passw)
    testpage.click_login_button()
    time.sleep(3)
    testpage.click_about_link()
    time.sleep(2)
    assert testpage.size_text() == True
