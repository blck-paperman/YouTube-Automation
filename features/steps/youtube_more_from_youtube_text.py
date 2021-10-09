from selenium.webdriver.common.by import By
from behave import when, then


@then('Verify "MORE FROM YOUTUBE" text present')
def verify_text_more_from_youtube_present(context):
    expected_result = "MORE FROM YOUTUBE"
    actual_result = context.driver.find_element(By.XPATH, "//yt-formatted-string[text()='More from YouTube']").text
    assert expected_result == actual_result, f'Expected "{expected_result}", but got "{actual_result}"'
