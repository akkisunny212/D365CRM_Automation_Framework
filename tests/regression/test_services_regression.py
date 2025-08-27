import pytest
import allure
import logging
from pages.services_page import ServicesPage

pytestmark = [pytest.mark.regression]

@allure.feature('Services Regression')
@pytest.mark.asyncio
async def test_submit_service_request_regression(page):
    """Regression: Submit a new service request and verify success."""
    logger = logging.getLogger('test_submit_service_request_regression')
    services_page = ServicesPage(page)
    await services_page.navigate_to_services()
    await services_page.submit_service('Regression Service')
    assert await services_page.is_request_submitted()
    logger.info('Regression service request submitted successfully.')
