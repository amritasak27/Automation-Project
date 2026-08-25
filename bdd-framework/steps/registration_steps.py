from pytest_bdd import scenarios, given, when, then, parsers

from pages.signup_page import SignupPage
from pages.account_info_page import AccountInfoPage
from utils.email_helper import unique_email

scenarios("../features/registration.feature")


@given("I am on the login page", target_fixture="signup_page")
def go_to_login_page(page):
    signup_page = SignupPage(page)
    signup_page.open("/login")
    return signup_page


@when("I sign up with a new unique email")
def signup_with_unique_email(signup_page):
    email = unique_email("bdd_registration")
    signup_page.start_signup("Jane Doe", email)


@when(parsers.parse('I start signup with name "{name}" and email "{email}"'))
def signup_with_given_details(signup_page, name, email):
    signup_page.start_signup(name, email)


@when("I complete the account information form", target_fixture="account_info_page")
def complete_account_info(page):
    account_info_page = AccountInfoPage(page)
    account_info_page.fill_and_submit()
    return account_info_page


@when(parsers.parse('I complete the account information form with title "{title}"'), target_fixture="account_info_page")
def complete_account_info_with_title(page, title):
    account_info_page = AccountInfoPage(page)
    account_info_page.fill_and_submit(title=title)
    return account_info_page


@then("my account should be created")
def assert_account_created(account_info_page):
    assert account_info_page.is_account_created()


@then("I should see an email already exists error")
def assert_email_exists_error(signup_page):
    assert signup_page.is_email_exists_error_visible()
