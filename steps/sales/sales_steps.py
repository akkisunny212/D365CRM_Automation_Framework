from behavex import given, when, then
from pages.login_page import LoginPage
from pages.sales_page import SalesPage

@given('I am logged in')
def step_login(context):
    LoginPage(context.page).login()

@when('I create a new lead')
def step_create_lead(context):
    SalesPage(context.page).create_lead()

@then('the lead should be saved successfully')
def step_lead_saved(context):
    assert SalesPage(context.page).is_lead_saved()
