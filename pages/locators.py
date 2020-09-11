from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    VIEW_BASKET = (By.CSS_SELECTOR, "span.btn-group>:nth-child(1)")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")


class LoginPageLocators:
    BUTTON_REGISTER = (By.CSS_SELECTOR, "div.col-sm-6.register_form button")
    CONFIRM_REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ALERT_ADDED_PRODUCT = (By.CSS_SELECTOR, "#messages>:nth-child(1)")
    ALERT_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages>:nth-child(3)")
    PRICE_IN_BASKET_TOTAL = (By.CSS_SELECTOR,
                             "#messages>:nth-child(3)>div.alertinner>:nth-child(1)>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>:nth-child(1)")
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, "#messages>:nth-child(1)>div.alertinner>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main .price_color")
