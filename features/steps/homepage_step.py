
from selenium.webdriver.common.by import By
from behave import then, given, when
from time import sleep




@given("Verify the name")
def name_verify(context):
    context.app.home_page.name_verify()


@then("Verify the URL")
def verify_home_page_url(context):
    context.app.home_page.verify_home_page_url('https://www.target.com/')
    sleep(10)