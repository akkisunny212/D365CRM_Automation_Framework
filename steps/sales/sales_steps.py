from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from pages.sales_page import SalesPage

scenarios('../../features/sales/sales.feature')

@given('I am logged in')
def step_login(browser):
    LoginPage(browser).login()

@when('I create a new lead')
def step_create_lead(browser):
    SalesPage(browser).create_lead()

@then('the lead should be saved successfully')
def step_lead_saved(browser):
    assert SalesPage(browser).is_lead_saved()
