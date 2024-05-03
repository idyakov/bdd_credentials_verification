from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.base_page import HelpPage
from pages.base_page import Page
from pages.header import Header
from pages.main_page import MainPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)
        self.help_page = HelpPage(driver)
