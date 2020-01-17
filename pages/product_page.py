# encoding: utf8

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_valid_alert(self):
        self.should_be_product_name_alert()
        self.should_be_product_price_alert()
        self.valid_product_name_alert()
        self.valid_product_price_alert()

    def should_be_product_name_alert(self):
        assert \
            self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_ALERT), \
            'no product name alert'

    def should_be_product_price_alert(self):
        assert \
            self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_ALERT), \
            'no product price alert'

    def valid_product_name_alert(self):
        product_name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_alert = self.get_element_text(*ProductPageLocators.PRODUCT_NAME_IN_ALERT)
        assert product_name == product_name_in_alert, \
            'got %s in alert. should be %s' % (product_name_in_alert, product_name)

    def valid_product_price_alert(self):
        product_price = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_alert = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE_IN_ALERT)
        assert product_price == product_price_in_alert, \
            'got %s in alert. should be %s' % (product_price_in_alert, product_price)
