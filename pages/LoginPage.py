from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from support.logger import logger

class LoginPage(Page):
    SIGN_IN_BUTTON_MAIN_PAGE = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    SING_IN_POPUP = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')
    TARGET_EMAIL = (By.CSS_SELECTOR, "[id*='username']")  # input email
    TARGET_PASSWORD = (By.CSS_SELECTOR, "[id*='password']")  # input password
    CLICK_SIGN_IN_USER = (By.CSS_SELECTOR,
                          "button[class='styles__StyledBaseButtonInternal-sc-ysboml-0 "
                          "styles__ButtonPrimary-sc-5fh6rr-0 styles__SignInButton-sc-q9vn5-4 hBqTSs bEdlr gCsDNn']")
    TARGET_VERIFY_ACCOUNT = (By.CSS_SELECTOR, 'span[class="styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3"]')
    TARGET_VERIFY_PASSWORD = (By.CSS_SELECTOR, 'div[data-test="authAlertDisplay"]')
    TARGET_VERIFY_USER = (By.CSS_SELECTOR, 'span[id="username--ErrorMessage"]')
    # click button SIgn in with password
    TARGET_NAME_VERIFICATION = (By.CSS_SELECTOR, "div[class*='styles__AlertDisplayStyles-sc-vw2fsn-0 gieqYR']")

    def click_sign_in(self):
        self.click(*self.SIGN_IN_BUTTON_MAIN_PAGE)

    def click_signin_popup(self):
        self.click(*self.SING_IN_POPUP)

    def input_credentials(self):
        logger.info(f'Input credentials')
        self.input_text('blabla@gmail.com', *self.TARGET_EMAIL)
        self.input_text('********@cZ+6AHD', *self.TARGET_PASSWORD)

    def click_sign_in_user(self):
        self.click(*self.CLICK_SIGN_IN_USER)
        sleep(5)

    def verify_account(self):
        self.click(*self.TARGET_VERIFY_ACCOUNT)
        sleep(5)

    def verify_wrong_email(self):  #### wrong email verification
        self.click(*self.TARGET_VERIFY_USER)
        sleep(5)

    def verify_not_find_email(self):
        text_message = self.find_element(*self.TARGET_NAME_VERIFICATION).text
        logger.info(f'error message - {text_message}')
        print(f'The error message is - "{text_message}"')
        sleep(5)
