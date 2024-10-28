from playwright.sync_api import Page

class IntegrationsPage:
    def __init__(self, page: Page):
        self.page = page

        self.selectors = {
            "integration_nav": '//*[@id="root"]/div[1]/div/div/div[2]/nav/div[2]/div/button[7]',
            "integrations_div": '//span[contains(text(), "Available Integrations")]',
            "email": '//h3[contains(text(), "Email")]',
            "viber": '//h3[contains(text(), "Viber")]',
            "telegram": '//h3[contains(text(), "Telegram")]',
            "line": '//h3[contains(text(), "Line")]',
            "live_chat": '//h3[contains(text(), "Live Chat Plugin")]',
            "live_chat_confirm": '[data-testid="button-element"]:text("Confirm Integration")',
            "live_chat_finish": '[data-testid="button-element"]:text("Finish")',
            "channel_next": '[data-testid="button-element"]:text("Next")',
            "close_icon": "path[d='M6.28 5.22a.75.75 0 00-1.06 1.06L8.94 10l-3.72 3.72a.75.75 0 101.06 1.06L10 11.06l3.72 3.72a.75.75 0 101.06-1.06L11.06 10l3.72-3.72a.75.75 0 00-1.06-1.06L10 8.94 6.28 5.22z']",
        }

    def goto_integrations(self):
        self.page.wait_for_selector(
            self.selectors["integration_nav"], state="visible"
        ).click()
        
    def check_available_integrations(self):
        self.page.wait_for_selector(
            self.selectors["integrations_div"], state="visible"
        ).click()
       
    def go_to_email(self):
        self.page.click(self.selectors["email"])
        self.page.locator(self.selectors["close_icon"]).click()
        
    def go_to_viber_telegram_line(self, integration):
        self.page.click(self.selectors[integration])
        self.page.wait_for_selector(
            self.selectors["channel_next"], state="visible"
        ).click()
        self.page.locator(self.selectors["close_icon"]).click()

    def go_to_live_chat_plugin(self):
        self.page.click(self.selectors["live_chat"])
        self.page.wait_for_selector(
            self.selectors["live_chat_confirm"], state="visible"
        ).click()
        self.page.wait_for_selector(
            self.selectors["live_chat_finish"], state="visible"
        ).click()
        self.page.wait_for_url('https://app.myalice.ai/integrations/integrated')
