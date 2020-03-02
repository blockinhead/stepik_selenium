# encoding: utf8

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'wrong login page url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            'no login form found'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            'no register form found'
