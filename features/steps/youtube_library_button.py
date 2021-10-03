from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "Library" button')
def click_button_library(context):
    context.driver.find_element(By.XPATH, "//a[@id='endpoint']//yt-formatted-string[text()='Library']").click()


@then('Verify "Library" button working')
def verify_library_button_worked(context):
    expected_result = 'https://www.youtube.com/feed/library'
    assert expected_result in context.driver.current_url, f'Expected {expected_result}, ' \
                                                          f'but got {context.driver.current_url}'
