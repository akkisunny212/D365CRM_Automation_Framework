from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from pages.services_page import ServicesPage

scenarios('../../features/services/services.feature')

@given('I am logged in')
def step_login(browser):
    LoginPage(browser).login()

@when('I submit a new service request')
def step_submit_service(browser):
    ServicesPage(browser).submit_request()

@then('the request should be submitted successfully')
def step_request_submitted(browser):
    assert ServicesPage(browser).is_request_submitted()
