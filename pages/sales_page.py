from playwright.sync_api import Page
from config.locators import SALES_LOCATORS
from config.urls import URLS
from .base_page import BasePage

class SalesPage(BasePage):
    def create_lead(self):
        self.navigate(URLS['sales'])
        self.fill(SALES_LOCATORS['lead_input'], 'Test Lead')
        self.click(SALES_LOCATORS['save_button'])

    def is_lead_saved(self):
        return self.page.is_visible('text=Lead saved')
