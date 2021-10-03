from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Explore YouTube page')
def open_youtube_explore(context):
    context.driver.get('https://www.youtube.com/feed/explore')


@when('Click "Home" button')
def click_button_home(context):
    context.driver.find_element(By.XPATH, "//a[@id='endpoint']//yt-formatted-string[text()='Home']").click()


@then('Verify "Home" button working')
def verify_home_button_worked(context):
    expected_result = 'https://www.youtube.com/'
    assert expected_result in context.driver.current_url, f'Expected {expected_result}, ' \
                                                          f'but got {context.driver.current_url}'
