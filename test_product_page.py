# encoding: utf8

import pytest
from .pages.product_page import ProductPage
import time

link_template = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer%d'
links_to_test = [link_template % i for i in range(10)]
links_to_test[7] = pytest.param(links_to_test[7], marks=pytest.mark.xfail)

single_page_to_test = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/']


@pytest.mark.parametrize('link', links_to_test)
def test_guest_can_add_product_to_basket(browser, link):
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
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
