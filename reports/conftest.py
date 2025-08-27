import pytest
import asyncio
from playwright.async_api import async_playwright

@pytest.fixture(scope='session')
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        yield page
        await browser.close()
