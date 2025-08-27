from behavex import given, when, then
from pages.login_page import LoginPage
from pages.services_page import ServicesPage

@given('I am logged in')
def step_login(context):
    login_page = LoginPage(context.page)
    context.page.loop.run_until_complete(login_page.login())

@when('I submit a new service request with name "Smoke Service"')
def step_submit_service(context):
    services_page = ServicesPage(context.page)
    context.page.loop.run_until_complete(services_page.submit_service('Smoke Service'))

@then('the request should be submitted successfully')
def step_request_submitted(context):
    services_page = ServicesPage(context.page)
    assert context.page.loop.run_until_complete(services_page.is_request_submitted())