from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "Gaming" button on left side')
def click_youtube_gaming_button(context):
    context.driver.find_element(By.XPATH, "//a[@id='endpoint']//yt-formatted-string[text()='Gaming']").click()


@then('Verify "Gaming" button worked')
def verify_youtube_gaming_button_worked(context):
    expected_result = "Gaming"
    actual_result = context.driver.find_element(By.XPATH, "//div[@id='inner-header-container']/"
                                                      "/yt-formatted-string[@id='title']").text
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
