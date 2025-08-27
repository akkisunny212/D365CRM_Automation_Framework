import asyncio
from playwright.async_api import async_playwright

def before_all(context):
    loop = asyncio.get_event_loop()
    context.playwright = loop.run_until_complete(async_playwright().start())
    context.browser = loop.run_until_complete(context.playwright.chromium.launch(headless=True))
    context.page = loop.run_until_complete(context.browser.new_page())
    context.page.loop = loop

def after_all(context):
    loop = context.page.loop
    loop.run_until_complete(context.page.close())
    loop.run_until_complete(context.browser.close())
    loop.run_until_complete(context.playwright.stop())
