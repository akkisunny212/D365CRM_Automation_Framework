from behavex import given, when, then
from pages.login_page import LoginPage
from pages.sales_page import SalesPage

@given('I am logged in')
def step_login(context):
    login_page = LoginPage(context.page)
    context.page.loop.run_until_complete(login_page.login())

@when('I create a new lead')
def step_create_lead(context):
    sales_page = SalesPage(context.page)
    context.page.loop.run_until_complete(sales_page.create_lead())

@then('the lead should be saved successfully')
def step_lead_saved(context):
    sales_page = SalesPage(context.page)
    assert context.page.loop.run_until_complete(sales_page.is_lead_saved())
