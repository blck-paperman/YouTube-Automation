from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "YouTube Premium" button on left side')
def click_youtube_premium_button(context):
    context.driver.find_element(By.XPATH, "//a[@id='endpoint']//yt-formatted-string[text()='YouTube Premium']").click()


@then('Verify "YouTube Premium" button worked')
def verify_youtube_premium_button_worked(context):
    link_premium = "https://www.youtube.com/premium"
    assert link_premium in context.driver.current_url, f'Expected {link_premium}, but got {context.driver.current_url}'
