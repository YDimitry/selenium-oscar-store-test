import pytest

from pages.product_page import ProductPage
offer = ['0','1','2','3','4','5','6','7','8','9']

@pytest.mark.parametrize('nr',offer)
def test_guest_can_add_product_to_basket(browser,nr):
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?'
    promo = 'promo=offer'+nr
    page = ProductPage(browser, link+promo)
    page.open()
    page.item_should_be_added_to_basket()

def test_guest_cant_see_success_message_after_adding_product_to_basket():
    """Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""
    pass

def test_guest_cant_see_success_message():
    """Открываем страницу товара
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""
    pass

def test_message_disappeared_after_adding_product_to_basket():
    """Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared"""
    pass

if __name__ == '__main__':
    pytest.main(['-rX','-v']) # rX