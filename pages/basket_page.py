# encoding: utf8

from .base_page import BasePage
from .locators import BasketPageLocators

BASKET_IS_EMPTY_MESSAGE = 'Your basket is empty'


class BasketPage(BasePage):

    def should_basket_be_empty(self):
        assert \
            self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'basket is not empty'

    def should_present_empty_message(self):
        msg = self.get_element_text(*BasketPageLocators.BASKET_CONTENT_SUMMARY)
        assert msg.startswith(BASKET_IS_EMPTY_MESSAGE), \
            'basket is empty message in not presented. got %s' % msg
