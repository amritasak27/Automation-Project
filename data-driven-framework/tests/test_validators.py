import pytest
from utils.validators import is_valid_phone, is_valid_zip


@pytest.mark.parametrize(
    "number, expected",
    [
        ("9876543210", True),   # exactly 10 digits
        ("12345", False),       # too short
        ("987654321099", False),  # too long
        ("98A7654B10", False),  # non-numeric
        ("", False),            # empty
    ],
)
def test_is_valid_phone(number, expected):
    assert is_valid_phone(number) == expected


@pytest.mark.parametrize(
    "zipcode, expected",
    [
        ("12345", True),   # exactly 5 digits
        ("123", False),    # too short
        ("123456789", False),  # too long
        ("AB123", False),  # non-numeric
        ("", False),       # empty
    ],
)
def test_is_valid_zip(zipcode, expected):
    assert is_valid_zip(zipcode) == expected
