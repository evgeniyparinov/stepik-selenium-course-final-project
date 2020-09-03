import time


def test_items(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(10)
    assert len(browser.find_elements_by_css_selector("button.btn-add-to-basket")) == 1,\
        "Неправильно выбран селектор (Селектор не уникален или элемент с таким селектором не был найден)"
