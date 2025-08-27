from playwright.sync_api import Page
from config.locators import SERVICES_LOCATORS
from config.urls import URLS
from .base_page import BasePage

class ServicesPage(BasePage):
    def submit_request(self):
        self.navigate(URLS['services'])
        self.fill(SERVICES_LOCATORS['service_input'], 'Test Service')
        self.click(SERVICES_LOCATORS['submit_button'])

    def is_request_submitted(self):
        return self.page.is_visible('text=Request submitted')
