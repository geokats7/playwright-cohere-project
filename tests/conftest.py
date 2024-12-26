import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from utils import get_random_title
from tests.page_objects.login import LoginPage

load_dotenv()

# Files in pytest_plugins will be available to every other file as if they were inside conftest.py.
# Those files must reside inside a package (there should be an __init.py__ file inside the parent folder)
# This is a way to organize shared fixtures in files that are not conftest.py
pytest_plugins = ["tests.page_object_fixtures"]

@pytest.fixture()
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://dashboard.cohere.com/welcome/login")
        login_page = LoginPage(page)
        login_page.fill_username("yorgoskatsaros@gmail.com")
        login_page.fill_password(os.getenv("PASSWORD"))
        login_page.click_login()

        # Accept all cookies
        page.get_by_role("button", name="Accept All").click()

        page.get_by_role("link", name="Dashboard").nth(2).click(button="right")
        assert page.get_by_role("link", name="Dashboard").nth(2).inner_text() == "Dashboard"
        
        yield page        
        page.get_by_role("button", name="").click()
        page.get_by_role("link", name="Log out").click()
        assert "login" in page.url
        
        page.close()
        context.close()
        browser.close()

# This function was created as a fixture to easily manage the the deletion of the file after the test is done.
@pytest.fixture()
def tmp_file(tmp_path):
    file = tmp_path / get_random_title()
    file.write_text("Test data") 
    yield file
    file.unlink()