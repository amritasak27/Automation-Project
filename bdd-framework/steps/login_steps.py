from pytest_bdd import scenarios, given, when, then, parsers

from pages.login_page import LoginPage

scenarios("../features/login.feature")


@given("I am on the login page", target_fixture="login_page")
def go_to_login_page(page):
    login_page = LoginPage(page)
    login_page.open("/login")
    return login_page


@when(parsers.parse('I log in with email "{email}" and password "{password}"'))
def perform_login(login_page, email, password):
    login_page.login(email, password)


@then("I should be logged in")
def assert_logged_in(login_page):
    assert login_page.is_logged_in()


@then("I should see a login error")
def assert_login_error(login_page):
    assert login_page.is_login_error_visible()
