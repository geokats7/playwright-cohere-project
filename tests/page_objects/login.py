class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username = page.get_by_placeholder("yourname@email.com")
        self.password = page.get_by_placeholder("••••••••••••")
        self.login_button = page.get_by_role("button", name="Log in ")
    
    def fill_username(self, username):
        self.username.click()
        self.username.fill(username)

    def fill_password(self, password):
        self.password.click()
        self.password.fill(password)
    
    def click_login(self):
        self.login_button.click()
    
    