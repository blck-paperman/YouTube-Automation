from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "Learning" button on left side')
def click_youtube_learning_button(context):
    context.driver.find_element(By.XPATH, "//a[@id='endpoint']//yt-formatted-string[text()='Learning']").click()


@then('Verify "Learning" button worked')
def verify_youtube_learning_button_worked(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@id='inner-header-container']//h1[@class="
                                                          "'style-scope ytd-topic-channel-details-renderer']").text
    expected_result = "Learning"
    assert expected_result == actual_result, f'Expected "{expected_result}", but got "{actual_result}"'
