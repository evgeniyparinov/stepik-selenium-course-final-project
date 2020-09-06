from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_add_to_basket(self):
        add_to_basket = \
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET),\
            "Button 'Add to basket' not found"

    def should_be_correspond_product_name(self):
        product_name_in_alert = \
            self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name_in_alert == product_name, \
            "A selected product does not correspond with a product name in the alert"

    def should_be_alert_product_has_been_added(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_ADDED_PRODUCT), \
            "Alert 'A product has been added to your basket' not found"

    def should_be_alert_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_BASKET_TOTAL), \
            "Alert 'basket total' is not found"

    def should_be_correspond_price(self):
        price_in_alert_total_basket = \
            self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert price_in_alert_total_basket == product_price, \
            "The price of a product does not correspond to the price in the basket"

    def should_be_not_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ADDED_PRODUCT), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_ADDED_PRODUCT), \
            "An element is not disappeared, but should be"
