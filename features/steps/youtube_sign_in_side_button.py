from selenium.webdriver.common.by import By
from behave import when, then


@when('Click "Sign in" button on left side')
def sign_in_side_button_click(context):
    context.driver.find_element(By.CSS_SELECTOR,
                                "ytd-guide-signin-promo-renderer a[href*='Faction_handle_signin']").click()


@then('Verify "Sign in" button worked')
def verify_sign_in_button_worked(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='jXeDnc ']//span[text()='Sign in']").text
    expected_result = "Sign in"
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
