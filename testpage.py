import logging

import yaml
from selenium.webdriver.common.by import By

from BaseApp import BasePage


class LocatorSearch:
    locs_dict = dict()
    with open('./locators.yaml', 'r') as f:
        locs = yaml.safe_load(f)
    for i in locs['xpath'].keys():
        locs_dict[i] = (By.XPATH, locs['xpath'][i])
    for i in locs['css'].keys():
        locs_dict[i] = (By.CSS_SELECTOR, locs['css'][i])


class OperationHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send '{word}' to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operate with {locator}")
            return False
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We found text {text} in field {element_name}")
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception while click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def look_header(self, locator, size, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        header = self.find_element(locator)
        if not header:
            return False
        try:
            header.value_of_css_property("font-size") == size
        except:
            logging.exception("Exception with fond header")
            return False
        logging.debug(f"Locked {element_name} font-size")
        return True

    def enter_login(self, word):
        self.enter_text_into_field(LocatorSearch.locs_dict['LOGIN_FIELD_LOCATOR'], word,
                                   description="Enter login")

    def enter_password(self, word):
        self.enter_text_into_field(LocatorSearch.locs_dict['PASSWORD_FIELD_LOCATOR'], word,
                                   description="Enter password")

    def size_text(self):
        return self.look_header(LocatorSearch.locs_dict['HEADER_TEXT_LOCATOR'], "32px", description="Header text")

    def get_err_text(self):
        return self.get_text_from_element(LocatorSearch.locs_dict['ERROR_LOGIN_LOCATOR'],
                                          description="Error login text")

    def profile_text(self):
        return self.get_text_from_element(LocatorSearch.locs_dict['HELLO_PROFILE_LOCATOR'],
                                          description="Profile text")

    def click_login_button(self):
        self.click_button(LocatorSearch.locs_dict['LOGIN_BUTTON_LOCATOR'], description="Click login button")

    def click_about_link(self):
        self.click_button(LocatorSearch.locs_dict['ABOUT_LOCATOR'], description="Click About")
