from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'В корзине присутствуют товары'

    def basket_empty_message_present(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        assert empty_basket_message == 'Your basket is empty. Continue shopping', 'нет сообщения о пустой корзине'