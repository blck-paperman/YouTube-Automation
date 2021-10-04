from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "News" button on left side')
def click_youtube_news_button(context):
    context.driver.find_element(By.XPATH, "//a[@id='endpoint']//yt-formatted-string[text()='News']").click()


@then('Verify "News" button worked')
def verify_youtube_button_worked(context):
    expected_result = "News"
    actual_result = context.driver.find_element(By.XPATH, "//div[@id='channel-header-container']"
                                                      "//ytd-channel-name[@id='channel-name']").text
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
