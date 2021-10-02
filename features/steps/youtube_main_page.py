from behave import then


@then('Verify that YouTube page opened')
def verify_search_worked(context):
    expected_result = 'https://www.youtube.com/'
    assert expected_result in context.driver.current_url, f'Expected {expected_result}, but got {context.driver.current_url}'
