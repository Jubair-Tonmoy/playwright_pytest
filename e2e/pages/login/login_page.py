from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.email_input = 'input[id="email"]'
        self.password_input = 'input[id="password"]'
        self.login_button = 'button[data-testid="button-element"]'

    def enter_email(self, email: str):
        self.page.fill(self.email_input, email)

    def enter_password(self, password: str):
        self.page.fill(self.password_input, password)

    def click_login(self):
        self.page.click(self.login_button)

    def login(self, email: str, password: str):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
