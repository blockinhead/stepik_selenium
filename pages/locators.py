# encoding: utf8

from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a.btn')


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


class BasketPageLocators(object):
    BASKET_CONTENT_SUMMARY = (By.CSS_SELECTOR, 'div.page div.content p')
    BASKET_ITEMS = (By.CSS_SELECTOR, 'div.basket-items')
