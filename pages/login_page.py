from playwright.sync_api import Page
from config.urls import URLS
import os
from dotenv import load_dotenv

load_dotenv('config/.env')

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self):
        self.page.goto(URLS['login'])
        self.page.fill('input[name="username"]', os.getenv('CRM_USERNAME'))
        self.page.fill('input[name="password"]', os.getenv('CRM_PASSWORD'))
        self.page.click('button#login')
