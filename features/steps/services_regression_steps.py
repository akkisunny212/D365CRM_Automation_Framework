from behave import given, when, then
from pages.login_page import LoginPage
from pages.services_page import ServicesPage

given('I am logged in to Services')
def step_login(context):
    login_page = LoginPage(context.page)
    context.loop.run_until_complete(login_page.login())

@when('I submit a new service request with name "Regression Service"')
def step_submit_service(context):
    services_page = ServicesPage(context.page)
    context.loop.run_until_complete(services_page.submit_service('Regression Service'))

@then('the regression service request should be submitted successfully')
def step_regression_request_submitted(context):
    services_page = ServicesPage(context.page)
    assert context.loop.run_until_complete(services_page.is_request_submitted())
