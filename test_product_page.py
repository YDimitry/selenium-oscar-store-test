import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
offer = ['0','1','2','3','4','5','6','7','8','9']

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# @pytest.mark.parametrize('nr',offer)
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser,nr):
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?'
    promo = 'promo=offer'+nr
    page = ProductPage(browser, link+promo)
    page.open()
    page.check_item_is_added_to_basket()

# @pytest.mark.xfail
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.shold_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    """Открываем страницу товара
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.shold_not_be_success_message()

# @pytest.mark.xfail
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared"""
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_is_disappeared()

# @pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста"""
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.basket_empty_message_present()



if __name__ == '__main__':
    pytest.main(['-rX','-v', '--language', 'en']) # rX