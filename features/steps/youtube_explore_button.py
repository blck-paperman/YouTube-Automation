from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open YouTube page')
def open_youtube(context):
    context.driver.get('https://www.youtube.com/')


@when('Click "Explore" button')
def click_search(context):
    context.driver.find_element(By.XPATH, "//a[@id='endpoint']//yt-formatted-string[text()='Explore']").click()


@then('Verify "Explore" button working')
def verify_search_worked(context):
    expected_result = 'https://www.youtube.com/feed/explore'
    assert 'https://www.youtube.com/feed/explore' in context.driver.current_url, f'Expected {expected_result}, but got {context.driver.current_url}'
