import logging

import yaml
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self):
        with open('./testdata.yaml') as f:
            testdata = yaml.safe_load(f)
        self.driver = webdriver.Chrome()
        self.base_url = testdata['address']

    def find_element(self, locator, time=5):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Can't find element by locator {locator}")
        except:
            logging.exception("Find element problem")
            element = None
        return element

    def get_element_property(self, locator, property):
        try:
            element = self.find_element(locator)
        except:
            logging.exception(f"Property {property} not found in element with locator {locator}")
            return None
        return element

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site")
            return None
        return start_browsing
