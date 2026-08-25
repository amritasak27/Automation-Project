class UserBuilder:
    """Builder pattern: registration payloads have many optional fields.
    A fluent builder avoids a constructor with 10 positional args and
    makes test intent explicit at the call site.

    Usage:
        user = (UserBuilder()
                .with_name("Jane Doe")
                .with_email("jane@example.com")
                .with_password("Secret123")
                .with_newsletter(True)
                .build())
    """

    def __init__(self):
        self._data = {
            "name": None,
            "email": None,
            "password": None,
            "newsletter": False,
            "address": None,
            "country": "United States",
        }

    def with_name(self, name: str) -> "UserBuilder":
        self._data["name"] = name
        return self

    def with_email(self, email: str) -> "UserBuilder":
        self._data["email"] = email
        return self

    def with_password(self, password: str) -> "UserBuilder":
        self._data["password"] = password
        return self

    def with_newsletter(self, subscribe: bool) -> "UserBuilder":
        self._data["newsletter"] = subscribe
        return self

    def with_address(self, address: str) -> "UserBuilder":
        self._data["address"] = address
        return self

    def with_country(self, country: str) -> "UserBuilder":
        self._data["country"] = country
        return self

    def build(self) -> dict:
        if not self._data["email"] or not self._data["name"]:
            raise ValueError("name and email are required to build a User")
        return dict(self._data)
