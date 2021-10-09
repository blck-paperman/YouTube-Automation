from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "Browse channels" button on left side')
def click_youtube_browse_channels_button(context):
    context.driver.find_element(By.XPATH, f"//a[@id='endpoint']//yt-formatted-string[text()='Browse channels']").click()


@then('Verify "Browse channels" button worked')
def verify_youtube_browse_channels_button_worked(context):
    link_browse_channels = "https://www.youtube.com/feed/guide_builder"
    assert link_browse_channels in context.driver.current_url, f'Expected "{link_browse_channels}", ' \
                                                               f'but got {context.driver.current_url}'
