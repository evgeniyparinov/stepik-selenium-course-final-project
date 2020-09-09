from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import time

"""
number_bugged_link = 7
pattern = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links = [f"{pattern}{i}" for i in range(10) if i != number_bugged_link]
bugged_link = pytest.param(f"{pattern}{number_bugged_link}",
                           marks=pytest.mark.xfail(reason="bug is found"))
links.insert(number_bugged_link, bugged_link)


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."

    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.go_to_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_alert_product_has_been_added()
    page.should_be_correspond_product_name()
    page.should_be_alert_basket_total()
    page.should_be_correspond_price()
"""


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_empty_basket()
    page.should_be_text_basket_is_empty()

"""
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.go_to_add_to_basket()
    page.should_be_not_success_message()
"""
"""
def test_guest_cant_see_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_not_success_message()
"""

"""
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
"""
"""
def test_can_go_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
 """

"""
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.go_to_add_to_basket()
    page.should_be_disappeared()
"""

