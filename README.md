# CRM_Framework_04

Playwright-based Python test automation framework for Microsoft D365CRM.

## Structure
- Features & Step Definitions per module
- Page Objects (BasePage, LoginPage, SalesPage, ServicesPage)
- Centralized config (locators, URLs, credentials)
- Logging & Reporting
- Test suites: functional, regression, smoke

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Run demo test: `pytest --alluredir=reports`
3. View report: Open `reports/index.html`

## Security
- Credentials are stored securely in `config/credentials.json` (use environment variables for production)

## Author
Senior Automation Tester
