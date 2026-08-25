import os
import pytest

from pages.signup_page import SignupPage
from pages.account_info_page import AccountInfoPage
from utils.data_reader import DataReader
from utils.email_helper import unique_email
from utils.validators import is_valid_phone, is_valid_zip

DATA_PATH = os.path.join(
    os.path.dirname(__file__), "..", "testdata", "registration_full_data.json"
)
raw_cases = DataReader().read(DATA_PATH)


def _build_params():
    """Wrap each data case in pytest.param, attaching an xfail mark for
    cases we already know the site won't reject (documented gaps) so the
    test report reads as 'expected failure: known gap' rather than a
    misleading red X.
    """
    params = []
    for case in raw_cases:
        marks = []
        if case.get("known_site_gap"):
            marks.append(pytest.mark.xfail(reason=case["gap_reason"], strict=True))
        params.append(pytest.param(case, id=case["case"], marks=marks))
    return params


@pytest.mark.parametrize("case", _build_params())
def test_registration(page, case):
    signup_page = SignupPage(page)
    signup_page.open("/login")

    email = unique_email(case["case"]) if case["email"] == "GENERATE" else case["email"]
    signup_page.start_signup(f"{case['first_name']} {case['last_name']}", email)

    # Duplicate-email case never reaches the account-info form.
    if case.get("expect_email_exists_error"):
        assert signup_page.is_email_exists_error_visible(), (
            "Expected 'Email Address already exist!' error for a known-registered email."
        )
        return

    account_info_page = AccountInfoPage(page)
    account_info_page.fill_account_info(case)
    account_info_page.submit()

    # 1. Real site behavior: does the account actually get created?
    assert account_info_page.is_account_created() == case["expect_account_created"], (
        f"Unexpected account-creation result for case '{case['case']}'."
    )

    # 2. Our own business rule, independent of what the site enforces.
    #    For known_site_gap cases this assertion is EXPECTED to fail
    #    (see the xfail mark above) - that failure IS the documented finding.
    assert is_valid_phone(case["mobile_number"]), (
        f"Mobile number '{case['mobile_number']}' violates the 10-digit business rule."
    )
    assert is_valid_zip(case["zipcode"]), (
        f"Zipcode '{case['zipcode']}' violates the 5-digit business rule."
    )
