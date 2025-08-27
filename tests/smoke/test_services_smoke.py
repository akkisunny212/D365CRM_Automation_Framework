import pytest
import allure
import logging
from pages.services_page import ServicesPage

pytestmark = [pytest.mark.smoke]

@allure.feature('Services Smoke')
@pytest.mark.asyncio
async def test_submit_service_request_smoke(page):
    """Smoke: Quick check for service request submission."""
    logger = logging.getLogger('test_submit_service_request_smoke')
    services_page = ServicesPage(page)
    await services_page.navigate_to_services()
    await services_page.submit_service('Smoke Service')
    assert await services_page.is_request_submitted()
    logger.info('Smoke service request submitted successfully.')
