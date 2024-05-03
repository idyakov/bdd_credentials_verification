from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class HomePage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    driver = webdriver.Chrome
    SIGN_IN_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    SING_IN_POPUP = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    TARGET_EMAIL = (By.CSS_SELECTOR, "[id*='username']")  # input email
    TARGET_PASSWORD = (By.CSS_SELECTOR, "[id*='password']")  # input password
    CLICK_SIGN_IN_USER = (By.CSS_SELECTOR,
                          "button[class='styles__StyledBaseButtonInternal-sc-ysboml-0 "
                          "styles__ButtonPrimary-sc-5fh6rr-0 styles__SignInButton-sc-q9vn5-4 hBqTSs bEdlr gCsDNn']")
    TARGET_VERIFY_ACCOUNT = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    # click button SIgn in with password
    TARGET_NAME_VERIFICATION = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')

    def name_verify(self):
        var_name = self.find_element(*self.TARGET_VERIFY_ACCOUNT).text
        print(var_name)
        sleep(5)

    def verify_home_page_url(self, expected_url):
        print(expected_url)
        self.wait.until(EC.url_contains(expected_url), message=f'URL verified')
