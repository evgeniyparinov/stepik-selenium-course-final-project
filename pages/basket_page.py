from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Text 'Your basket is not empty' is not presented"

    def should_be_text_basket_is_empty(self):
        text_empty_basket =\
            self.browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET).text
        assert text_empty_basket == text_empty_basket, "Your basket is not empty"
