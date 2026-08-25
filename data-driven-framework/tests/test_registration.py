import os
import pytest

from pages.signup_page import SignupPage
from utils.data_reader import DataReader
from models.user_builder import UserBuilder

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "testdata", "registration_data.csv")
signup_cases = DataReader().read(DATA_PATH)


@pytest.mark.parametrize("case", signup_cases, ids=[c["case"] for c in signup_cases])
def test_signup_starts_account_form(page, case):
    user = (
        UserBuilder()
        .with_name(case["name"])
        .with_email(case["email"])
        .build()
    )

    signup_page = SignupPage(page)
    signup_page.open("/login")
    signup_page.start_signup(user["name"], user["email"])

    expect_visible = case["expect_form_visible"] == "true"
    assert signup_page.is_account_info_form_visible() == expect_visible
