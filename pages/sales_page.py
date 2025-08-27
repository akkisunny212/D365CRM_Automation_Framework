from playwright.async_api import Page
from config.sales_locators import SALES_PAGE
from config.urls import URLS

class SalesPage:
    def __init__(self, page: Page):
        self.page = page

    async def create_lead(self):
        await self.page.goto(URLS['sales'])
        await self.page.fill(SALES_PAGE['lead_input'], 'Test Lead')
        await self.page.click(SALES_PAGE['save_button'])

    async def is_lead_saved(self):
        return await self.page.is_visible(SALES_PAGE['success_message'])
