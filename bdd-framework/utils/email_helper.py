import time


def unique_email(prefix: str) -> str:
    return f"{prefix}.{int(time.time() * 1000)}@example.com"
