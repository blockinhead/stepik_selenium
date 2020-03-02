# encoding: utf8

import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link_template = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer%d'
links_to_test = [link_template % i for i in range(10)]
links_to_test[7] = pytest.param(links_to_test[7], marks=pytest.mark.xfail)

single_page_to_test = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/']


@pytest.mark.user_product
class TestUserAddToBasketFromProductPage(object):

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        t = str(time.time())
        login_page.register_new_user(t + '@fakemail.com', t[:10])
        login_page.should_be_authorized_user()

        self.product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, self.product_link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, self.product_link)
        product_page.open()
        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.should_be_valid_alert()


@pytest.mark.need_review
@pytest.mark.parametrize('link', links_to_test[:1])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_valid_alert()
    # time.sleep(20)


@pytest.mark.xfail(reason='success message does not disappear, its okey')
@pytest.mark.parametrize('link', single_page_to_test)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.parametrize('link', single_page_to_test)
def test_guest_cant_see_success_message(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason='success message does not disappear, its okey')
@pytest.mark.parametrize('link', single_page_to_test)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_basket_be_empty()
    basket_page.should_present_empty_message()
