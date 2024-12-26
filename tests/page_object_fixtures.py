import pytest
from tests.page_objects.login import LoginPage
from tests.page_objects.home import HomePage
from tests.page_objects.chat import ChatPage

# This fixture should be used when testing the login page itself
@pytest.fixture()
def login_page(page):
    return LoginPage(page)

@pytest.fixture()
def home_page(page):
    return HomePage(page)

@pytest.fixture()
def chat_page(page):
    return ChatPage(page)


