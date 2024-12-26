class HomePage:

    def __init__(self, page):
        self.page = page
        self.chat_link = page.get_by_role("link", name="Chat", exact=True)
        self.chat_button = page.get_by_role("button", name="Try now ")
        self.dashboard_link = page.get_by_role("link", name="Dashboard").nth(2)

    def click_chat(self):
        self.chat_link.click()

    def click_try_now(self):
        self.chat_button.click()

    