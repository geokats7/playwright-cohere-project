import pytest
from playwright.sync_api import expect

def test_scenario_01(page):
    page.get_by_role("link", name="Chat", exact=True).click()
    page.get_by_role("button", name="Try now ").click()
    page.get_by_placeholder("Message...").click()
    page.get_by_placeholder("Message...").fill("What is the first name of Einstein?")
    page.get_by_role("button", name="").click()
    response = page.locator("xpath=//main/section/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div[@data-component='MessageContent']/div/div/p").inner_text()
    assert "albert" in response.lower(), f"Expected response to contain 'albert', but got '{response}'"


def test_scenario_02(page, tmp_file):
    page.get_by_role("link", name="Chat", exact=True).click()
    page.get_by_role("button", name="Try now ").click()
    file_chooser = page.locator("xpath=//*[@id=\"message-list\"]/div[2]/div/div/div[1]/input")
    file_chooser.set_input_files(tmp_file)
    expect(page.get_by_text("txt •9 bytes")).to_be_visible()
    page.get_by_placeholder("Message...").click()
    query = "Describe the contents of the file"
    page.get_by_placeholder("Message...").fill(query)
    page.get_by_role("button", name="").click()
    assert "test data" in page.locator("xpath=//main/section/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/div[@data-component='MessageContent']/div/div/p").inner_text().lower()


    