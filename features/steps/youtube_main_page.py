from behave import then


@then('Verify that YouTube page opened')
def verify_main_page_worked(context):
    expected_result = 'https://www.youtube.com/'
    assert expected_result in context.driver.current_url, f'Expected {expected_result}, ' \
                                                          f'but got {context.driver.current_url}'
