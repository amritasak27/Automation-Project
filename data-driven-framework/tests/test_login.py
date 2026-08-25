import os
import pytest

from pages.login_page import LoginPage
from utils.data_reader import DataReader

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "testdata", "login_data.json")
login_cases = DataReader().read(DATA_PATH)


@pytest.mark.parametrize("case", login_cases, ids=[c["case"] for c in login_cases])
def test_login(page, case):
    login_page = LoginPage(page)
    login_page.open("/login")

    login_page.login(case["email"], case["password"])

    if case["expect_success"]:
        assert login_page.is_logged_in(), f"Expected successful login for case: {case['case']}"
    else:
        assert login_page.is_login_error_visible(), f"Expected login error for case: {case['case']}"
