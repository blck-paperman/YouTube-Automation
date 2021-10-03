from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "YouTube" button')
def click_youtube_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a#logo div.style-scope.ytd-topbar-logo-renderer").click()


@then('Verify "YouTube" button working')
def verify_youtube_button_worked(context):
    expected_result = 'https://www.youtube.com/'
    assert expected_result in context.driver.current_url, f'Expected {expected_result}, ' \
                                                          f'but got {context.driver.current_url}'
