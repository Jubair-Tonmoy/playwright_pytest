import allure
from tests.base_test import login
from pages.inbox.fb_feed_page import FBFeedPage
from utils.config_loader import load_config

@allure.feature("Facebook Feed Functionality")
@allure.story("User sends message via chatbox")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://your_project_tracking_url", name="Project Tracking Link")
@allure.description(
    "This test verifies that the agent can reply to comments in the facebook feed."
)

def test_commentbox(browser_context):
    page = browser_context

    with allure.step("Log in to the application"):
        login(page)

    with allure.step("Load configuration and navigate to chatbox"):
        fb_feed_page = FBFeedPage(page)
        config = load_config()
        base_url = config["base_url"]
        fb_feed_page.goto_fb_feed()

    with allure.step("Verify comment section URL and send message"):
        # Replace with your project id
        page.wait_for_url(f"{base_url}/projects/13648/inbox")
        fb_feed_page.comment_send_confirm("Good day from jubair ahmed khan tonmoy")
        page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

    # with allure.step("Verify comment section URL and send private reply"):
    #     # Replace with your project id
    #     page.wait_for_url(f"{base_url}/projects/1153/inbox")
    #     fb_feed_page.private_reply_send_confirm("Hello from jubair ahmed khan")
    #     page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step("Send imoji and verify delivery"):
        fb_feed_page.imoji_send_confirm()

    with allure.step("Send attachments and verify delivery"):
        # fb_feed_page.handle_attachment_modal()
        fb_feed_page.upload_image("e2e/data/images/2mb.jpg")
        # fb_feed_page.upload_image("e2e/data/images/6mb.jpg")
       
    with allure.step("Send saved reply and verify delivery"):
        fb_feed_page.saved_reply_send_confirm()

    with allure.step("Send private reply"):
        fb_feed_page.private_reply_send_confirm("Dear, this is a private reply")

    allure.attach(
        page.screenshot(),
        name="Facebook Feed Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
