from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "Spotlight" button on left side')
def click_spotlight_button(context):
    context.driver.find_element(By.XPATH, f"//a[@id='endpoint']//yt-formatted-string[text()='Spotlight']").click()


@then('Verify "Spotlight" button worked')
def verify_youtube_fashion_and_beauty_button_worked(context):
    link_spotlight = "https://www.youtube.com/channel/UCBR8-60-B28hp2BmDPdntcQ"
    assert link_spotlight in context.driver.current_url, f' Expected {link_spotlight}, ' \
                                                         f'but got {context.driver.current_url}'
