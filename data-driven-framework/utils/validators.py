"""
Field validators encoding OUR business rules for the registration form.

Note: automationexercise.com does NOT enforce these rules server-side or
client-side - it accepts any non-empty mobile_number/zipcode. These
validators exist so the test suite can independently verify data against
a spec, and flag cases where the application under test is more permissive
than the spec (a real, reportable finding - not a framework bug).
"""


def is_valid_phone(number: str) -> bool:
    """Business rule: mobile number must be exactly 10 digits, digits only."""
    return number.isdigit() and len(number) == 10


def is_valid_zip(zipcode: str) -> bool:
    """Business rule: zipcode must be exactly 5 digits, digits only."""
    return zipcode.isdigit() and len(zipcode) == 5
