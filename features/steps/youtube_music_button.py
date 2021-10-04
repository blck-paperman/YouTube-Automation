from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "Music" button on left side')
def youtube_music_button(context):
    context.driver.find_element(By.XPATH, "//a[@id='endpoint']//yt-formatted-string[text()='Music']").click()


@then('Verify "Music" button worked')
def verify_youtube_music_button_worked(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@id='inner-header-container']/"
                                                          "/yt-formatted-string[@id='title']").text
    expected_result = "Music"
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
