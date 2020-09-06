from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ALERT_ADDED_PRODUCT = (By.CSS_SELECTOR, "#messages>:nth-child(1)")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>:nth-child(1)")
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, "#messages>:nth-child(1)>div.alertinner>strong")
    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages>:nth-child(3)")
    PRICE_IN_BASKET_TOTAL = (By.CSS_SELECTOR,
                             "#messages>:nth-child(3)>div.alertinner>:nth-child(1)>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main .price_color")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
