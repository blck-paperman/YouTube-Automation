from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "History" button')
def click_history_button(context):
    context.driver.find_element(By.XPATH, "//a[@id='endpoint']//yt-formatted-string[text()='History']").click()


@then('Verify "History" button working')
def verify_history_button_worked(context):
    expected_result = 'https://www.youtube.com/feed/history'
    assert expected_result in context.driver.current_url, f'Expected {expected_result}, ' \
                                                          f'but got {context.driver.current_url}'