from pages.login.login_page import LoginPage
from utils.config_loader import load_config, load_login_data


def login(browser_context):
    page = browser_context

    config = load_config()
    login_data = load_login_data()

    base_url = config["base_url"]
    email = login_data["email"]
    password = login_data["password"]

    login_page = LoginPage(page)

    page.goto(f"{base_url}")
    login_page.login(email, password)
    page.wait_for_url(f"{base_url}/dashboard")
