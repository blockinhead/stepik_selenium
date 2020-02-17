# encoding: utf8

from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')


class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, 'div.alert-success div.alertinner strong')
    PRODUCT_PRICE_IN_ALERT = (By.CSS_SELECTOR, 'div.alert-info div.alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')
