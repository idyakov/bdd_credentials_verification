from selenium.webdriver.common.by import By
from behave import then, given, when
from time import sleep


@given('Open Target help page')
def open_help_page(context):
    context.app.help_page.open_help_page()


#
#
@given("Search for a topic")
def search_for_a_topic(context):
    context.app.help_page.dropdown_menu()


@given("Verify dropdown page is opened")
def verify_page(context):
    context.app.help_page.verify_page('https://help.target.com/help/SubCategoryArticle?childcat=Print+a+receipt'
                                      '&parentcat=Orders+%26+Purchases&searchQuery=')


#
@given("Verification uncorrected credential functionality")
def verif_incorrect_email(context):
    context.app.login_page.verify_not_find_email()
#
#
# @given("Click sign in user")
# def click_sign_in_user(context):
#     context.app.login_page.click_sign_in_user()
#
#
# @then("Verify the account")
# def verify_account(context):
#     context.app.login_page.verify_account()
#
