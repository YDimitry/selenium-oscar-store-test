from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR,'#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR,'div.basket-mini a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '#basket_formset')

class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR,'#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR,'#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASS_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class ProducPageLocators:
    ITEM_NAME = (By.CSS_SELECTOR,'div.product_main h1')
    ITEM_PRICE = (By.CSS_SELECTOR,'div.product_main p.price_color')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR,'button.btn-add-to-basket')
    GOOD_ADDED_MESSAGE = (By.CSS_SELECTOR,'#messages div.alertinner strong')
