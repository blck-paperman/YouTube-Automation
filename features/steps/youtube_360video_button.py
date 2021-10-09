from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "360° Video" button on left side')
def click_360video_button(context):
    context.driver.find_element(By. XPATH, f"//a[@id='endpoint']//yt-formatted-string[text()='360° Video']").click()


@then('Verify "360° Video" button worked')
def verify_360video_button_worked(context):
    expected_result = "Virtual Reality"
    actual_result = context.driver.find_element(By.XPATH, "//div[@id='channel-header-container']"
                                                      "//ytd-channel-name[@id='channel-name']").text
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
