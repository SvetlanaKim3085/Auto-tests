from selenium.common.exceptions import NoSuchElementException


def test_add_to_cart_button_is_presence(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    try:
        browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
    except NoSuchElementException:
        raise AssertionError('Did not matched')
    import time; time.sleep(10)
