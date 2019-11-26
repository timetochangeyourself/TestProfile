from selenium import webdriver
from src.header import HeaderPage
from src.login  import LoginPage


class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome('E:\Webdriver\chromedriver')
        self.login = LoginPage(self.driver)
        self.header = HeaderPage(self.driver)

    def test_login_to_olx_page_object(self):
        self.login.open()
        assert self.login.at_page()
        self.login.login_to_olx()
        assert self.header.at_page()

    def teardown_method(self):
        self.driver.close()