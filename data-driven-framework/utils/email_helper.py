import time


def unique_email(prefix: str) -> str:
    """automationexercise.com rejects re-registering an existing email, and
    accounts persist between test runs. Generating a timestamp-suffixed
    email per run keeps registration tests repeatable without manual cleanup.
    """
    return f"{prefix}.{int(time.time() * 1000)}@example.com"
