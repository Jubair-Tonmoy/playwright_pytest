from playwright.sync_api import Page

class FBFeedPage:
    def __init__(self, page: Page):
        self.page = page

        self.selectors = {
            "chatbox_nav": '//*[@id="root"]/div[1]/div/div/div[2]/nav/div[2]/div/button[3]',
            "agent_div": '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[3]',
            "convo_bar": '[id="conversation-bar"]',
            "fb_feed_textarea": '[id="reply-input"]',
            "fb_feed_imoji": '//*[@id="headlessui-popover-button-13"]',
            "fb_feed_grinning_face":'//*[@id="headlessui-popover-panel-14"]/aside/div[3]/section/ul[1]/li[1]/button',
            "fb_feed_attachment": '//*[@id="headlessui-popover-button-15"]',
            "attachment_dropzone": '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]/div',
            "attachment_list": '[role="listitem"]',
            "close_modal": '[title="Close Modal"]',
            "attachment_send": '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[4]/div[1]/div[2]/button',
            "fb_feed_saved_reply":'//*[@id="headlessui-popover-button-17"]',
            "fb_feed_saved_reply_keyword":'//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div[3]/div[3]/div/div/div/div[2]/div/div[1]',
            "fb_feed_private_reply" : '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div[3]/div[1]/div/div/nav/div[2]',
            "fb_feed_send": '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/button',
        }


    def goto_fb_feed(self):
        self.page.wait_for_selector(self.selectors["agent_div"], state="visible")
        self.page.click(self.selectors["chatbox_nav"])

    def comment_send_confirm(self, message: str):
        self.page.wait_for_selector(self.selectors["fb_feed_textarea"], state="visible")
        self.page.fill(self.selectors["fb_feed_textarea"], message)
        self.page.click(self.selectors["fb_feed_send"])
        self.page.wait_for_selector(f'//p[contains(text(), "{message}")]', state="visible")

    def imoji_send_confirm(self):
        self.page.click(self.selectors["fb_feed_imoji"])
        self.page.wait_for_selector(self.selectors["fb_feed_grinning_face"], state="visible").click()
        self.page.click(self.selectors["fb_feed_send"])

    def upload_file(self, file_type: str, file_path: str):
        self.page.wait_for_selector(self.selectors["fb_feed_attachment"], state="visible").click()
        # self.page.click(self.selectors["fb_feed_attachment"])
        # self.page.click(self.selectors[f"attachment_{file_type}"])
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_text("Upload").click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        self.page.click(self.selectors["attachment_send"])
        self.page.wait_for_selector(
            self.selectors["attachment_dropzone"], state="hidden"
        )

    def upload_image(self, file_path: str):
        self.upload_file("image", file_path)

    # def handle_attachment_modal(self):
    #     # Wait for the attachment list to be visible
    #     self.page.wait_for_selector(self.selectors["attachment_list"], state="visible")

    def saved_reply_send_confirm(self):
        self.page.click(self.selectors["fb_feed_saved_reply"])
        self.page.wait_for_selector(self.selectors["fb_feed_saved_reply_keyword"], state="visible").click()
        self.page.click(self.selectors["fb_feed_send"])
        
    def private_reply_send_confirm(self, message: str):
        self.page.click(self.selectors["fb_feed_private_reply"])
        self.page.wait_for_selector(self.selectors["fb_feed_textarea"], state="visible")
        self.page.fill(self.selectors["fb_feed_textarea"], message)
        self.page.click(self.selectors["fb_feed_send"])
        self.page.wait_for_selector(f'//p[contains(text(), "{message}")]')
        
