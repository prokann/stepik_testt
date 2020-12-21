import time


class Test_button:
    def test_find_button(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
        time.sleep(10)
        assert browser.find_element_by_css_selector("button.btn-add-to-basket")

