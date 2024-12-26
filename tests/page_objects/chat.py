class ChatPage:

    def __init__(self, page):
        self.page = page
        self.message_input = page.get_by_placeholder("Message...")
        self.send_button = page.get_by_role("button", name="")
        self.response_message = page.locator("xpath=//main/section/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div[@data-component='MessageContent']/div/div/p")

    def send_message(self, message):
        self.message_input.click()
        self.message_input.fill(message)
        self.send_button.click()

    def upload_file(self, file_path):
        file_chooser = self.page.locator("xpath=//*[@id=\"message-list\"]/div[2]/div/div/div[1]/input")
        file_chooser.set_input_files(file_path)
        return file_chooser