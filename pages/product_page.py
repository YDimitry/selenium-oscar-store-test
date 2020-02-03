from pages.base_page import BasePage
from pages.locators import ProducPageLocators

class ProductPage(BasePage):
    def item_should_be_added_to_basket(self):
        item_name = self.get_item_name()
        item_price = self.get_item_price()
        self.add_to_basket()
        message = self.get_result_message()
        self.item_should_be_added(message)
        self.added_item_name_should_be_the_same(message,item_name)
        self.added_item_price_shold_be_the_same(message,item_price)

    def get_item_name(self):
        return self.browser.find_element(*ProducPageLocators.ITEM_NAME).text

    def get_item_price(self):
        return self.browser.find_element(*ProducPageLocators.ITEM_NAME).text

    def add_to_basket(self):
        btn = self.browser.find_element(*ProducPageLocators.ADD_TO_BASKET_BUTTON)
        btn.click()
        self.solve_quiz_and_get_code()

    def get_result_message(self):
        return list(map(lambda el:el.text, self.browser.find_elements(*ProducPageLocators.GOOD_ADDED_MESSAGE)))


    def item_should_be_added(self,message):
        assert len(message) != 0, 'Товар не был добавлен в корзину'

    def added_item_name_should_be_the_same(self,message,item_name):
        assert item_name in message, 'название добавленного товара отличается'

    def added_item_price_shold_be_the_same(self,message,item_price):
        assert item_price in message, 'стоимость добавленного товара отличается'