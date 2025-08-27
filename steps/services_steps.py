from behavex import given, when, then
from pages.login_page import LoginPage
from pages.services_page import ServicesPage

# Regression scenario
@given('I am logged in')
def step_login(context):
    login_page = LoginPage(context.page)
    context.page.loop.run_until_complete(login_page.login())

@when('I submit a new service request with name "Regression Service"')
def step_submit_service_regression(context):
    services_page = ServicesPage(context.page)
    context.page.loop.run_until_complete(services_page.submit_service('Regression Service'))

@then('the request should be submitted successfully')
def step_request_submitted_regression(context):
    services_page = ServicesPage(context.page)
    assert context.page.loop.run_until_complete(services_page.is_request_submitted())

# Smoke scenario
@when('I submit a new service request with name "Smoke Service"')
def step_submit_service_smoke(context):
    services_page = ServicesPage(context.page)
    context.page.loop.run_until_complete(services_page.submit_service('Smoke Service'))

@then('the request should be submitted successfully')
def step_request_submitted_smoke(context):
    services_page = ServicesPage(context.page)
    assert context.page.loop.run_until_complete(services_page.is_request_submitted())