from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "Fashion & Beauty" button on left side')
def click_youtube_fashion_and_beauty_button(context):
    context.driver.find_element(By.XPATH, "//a[@id='endpoint']//yt-formatted-string[text()='Fashion & Beauty']").click()


@then('Verify "Fashion & Beauty" button worked')
def verify_youtube_fashion_and_beauty_button_worked(context):
    expected_result = "Fashion & Beauty"
    actual_result = context.driver.find_element(By.XPATH, "//div[@id='inner-header-container']//h1[@class="
                                                          "'style-scope ytd-topic-channel-details-renderer']").text
    assert expected_result == actual_result, f'Expected "{expected_result}", but got "{actual_result}"'
