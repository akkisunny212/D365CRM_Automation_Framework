from playwright.async_api import Page
from config.urls import URLS
import os
from dotenv import load_dotenv

load_dotenv('config/.env')

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    async def login(self):
        await self.page.goto(URLS['login'])
        await self.page.fill('input[name="username"]', os.getenv('CRM_USERNAME'))
        await self.page.fill('input[name="password"]', os.getenv('CRM_PASSWORD'))
        await self.page.click('button#login')
