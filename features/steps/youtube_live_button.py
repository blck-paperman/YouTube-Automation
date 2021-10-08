from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "Live" button on left side')
def click_youtube_live_button(context):
    context.driver.find_element(By.XPATH, "//a[@id='endpoint']//yt-formatted-string[text()='Live']").click()


@then('Verify "Live" button worked')
def verify_youtube_live_button_worked(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@id='channel-header-container']"
                                                      "//ytd-channel-name[@id='channel-name']").text
    expected_result = "Live"
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
