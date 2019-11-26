import time

link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button(browser):
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 100);")
    button=browser.find_element_by_css_selector("#add_to_basket_form > button")
    button_name=button.text
    assert "Añadir al carrito"==button_name, f"Button_name did not match"