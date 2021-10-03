from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "Subscriptions" button')
def click_button_subscriptions(context):
    context.driver.find_element(By.XPATH, "//a[@id='endpoint']//yt-formatted-string[text()='Subscriptions']").click()


@then('Verify "Subscriptions" button working')
def verify_subscriptions_button_worked(context):
    expected_result = 'https://www.youtube.com/feed/subscriptions'
    assert expected_result in context.driver.current_url, f'Expected {expected_result}, ' \
                                                          f'but got {context.driver.current_url}'
