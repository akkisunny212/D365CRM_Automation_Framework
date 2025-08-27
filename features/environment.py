from playwright.async_api import async_playwright

def before_all(context):
    import asyncio
    context.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(context.loop)
    context.playwright = context.loop.run_until_complete(async_playwright().start())
    context.browser = context.loop.run_until_complete(context.playwright.chromium.launch(headless=True))
    context.page = context.loop.run_until_complete(context.browser.new_page())

def after_all(context):
    context.loop.run_until_complete(context.page.close())
    context.loop.run_until_complete(context.browser.close())
    context.loop.run_until_complete(context.playwright.stop())
