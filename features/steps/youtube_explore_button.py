from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open YouTube page')
def open_youtube(context):
    context.driver.get('https://www.youtube.com/')


@when('Click "Explore" button')
def click_button_explore(context):
    context.driver.find_element(By.XPATH, "//a[@id='endpoint']//yt-formatted-string[text()='Explore']").click()


@then('Verify "Explore" button working')
def verify_explore_button_worked(context):
    expected_result = 'https://www.youtube.com/feed/explore'
    assert expected_result in context.driver.current_url, f'Expected {expected_result}, ' \
                                                          f'but got {context.driver.current_url}'
