import time

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'accounts/login/' in self.browser.current_url, 'Login url incorrect'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not present'

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        reg_pass = self.browser.find_element(*LoginPageLocators.REGISTER_PASS)
        reg_pass_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_CONFIRM)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        reg_email.send_keys(email)
        reg_pass.send_keys(password)
        reg_pass_confirm.send_keys(password)
        reg_button.click()
