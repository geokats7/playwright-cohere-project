import pytest
from playwright.sync_api import expect

def test_scenario_01(page, home_page, chat_page):
    home_page.click_chat()
    home_page.click_try_now()
    chat_page.send_message("What is the first name of Einstein?")
    response = chat_page.response_message.inner_text()
    assert "albert" in response.lower(), f"Expected response to contain 'albert', but got '{response}'"

def test_scenario_02(page, tmp_file, home_page, chat_page):
    home_page.click_chat()
    home_page.click_try_now()
    chat_page.upload_file(tmp_file)
    expect(page.get_by_text("txt •9 bytes")).to_be_visible()
    chat_page.send_message("Describe the contents of the file")
    response = chat_page.response_message.inner_text()
    assert "test data" in response.lower()


    