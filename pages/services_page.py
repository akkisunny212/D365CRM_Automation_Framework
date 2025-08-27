from playwright.async_api import Page
from config.services_locators import SERVICES_PAGE
from config.urls import URLS

class ServicesPage:
    def __init__(self, page: Page):
        self.page = page

    async def navigate_to_services(self):
        await self.page.goto(URLS['services'])

    async def submit_service(self, service_name):
        await self.page.fill(SERVICES_PAGE['service_input'], service_name)
        await self.page.click(SERVICES_PAGE['submit_button'])

    async def is_request_submitted(self):
        return await self.page.is_visible(SERVICES_PAGE['success_message'])
