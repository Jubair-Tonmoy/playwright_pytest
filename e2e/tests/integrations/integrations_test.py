import allure
from tests.base_test import login
from pages.integrations.integrations_page import IntegrationsPage


@allure.feature("Integrations Functionality")
@allure.story("User integrates with stores")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://your_project_tracking_url", name="Project Tracking Link")
@allure.description("This test verifies that the user can integrate with stores.")
def test_integrations(browser_context):
    page = browser_context

    with allure.step("Log in to the application"):
        login(page)

    with allure.step("Load configuration and navigate to integrations"):
        integrations_page = IntegrationsPage(page)
        integrations_page.goto_integrations()

    with allure.step("See available integrations"):
        integrations_page.check_available_integrations()

    with allure.step("Verify Channel integrations"):
        with allure.step("Verify email integrations"):
            integrations_page.go_to_email()

        integrations =[
            "viber",
            "telegram",
            "line",
        ]

        for integration in integrations:
            with allure.step(f"Verify {integration} integration"):
                integrations_page.go_to_viber_telegram_line(integration)
 
        with allure.step("Verify live chat plugin integrations"):
            integrations_page.go_to_live_chat_plugin()

    allure.attach(
        page.screenshot(),
        name="Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )