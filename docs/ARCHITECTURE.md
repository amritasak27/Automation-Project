# Architecture & Design Patterns

This document exists mainly for interview conversations — it maps each design pattern used
to the file that implements it and why it was chosen over the naive alternative.

## 1. Page Object Model (both frameworks)

Every page has a `pages/*.py` class with:
- Locators as class attributes (or `@property` if built dynamically)
- Action methods (`login()`, `add_to_cart()`) — no assertions live here
- A shared `BasePage` holding common waits/actions (`click`, `fill`, `is_visible`, explicit waits)

Assertions live in the test/step layer, not in page objects — keeps page objects reusable
across both frameworks and prevents "assertion soup" inside business methods.

## 2. Factory Pattern — `utils/driver_factory.py`

```python
class BrowserFactory:
    @staticmethod
    def get_browser(playwright, browser_name: str):
        if browser_name == "chromium":
            return playwright.chromium.launch()
        elif browser_name == "firefox":
            return playwright.firefox.launch()
        elif browser_name == "webkit":
            return playwright.webkit.launch()
        raise ValueError(f"Unsupported browser: {browser_name}")
```

Why: cross-browser support without `if/elif` chains scattered through fixtures. Talking point:
"adding a new browser target is a one-line change in one file."

## 3. Singleton Pattern — `utils/config_reader.py`

Config (base URL, timeouts, browser) is read from YAML once and cached, so every test/page object
gets the same config object instead of re-reading the file per test.

## 4. Strategy Pattern — `data-driven-framework/utils/data_reader.py`

```python
class DataReader:
    def read(self, path: str):
        if path.endswith(".json"):
            return self._read_json(path)
        elif path.endswith(".csv"):
            return self._read_csv(path)
        raise ValueError("Unsupported data format")
```

Why: tests don't care whether data comes from JSON or CSV — swapping the data source strategy
doesn't touch test code. Easy to extend to Excel/DB later.

## 5. Builder Pattern — `data-driven-framework/models/user_builder.py`

```python
user = (UserBuilder()
        .with_name("Jane Doe")
        .with_email("jane@example.com")
        .with_password("Secret123")
        .build())
```

Why: registration payloads have many optional fields (address, DOB, newsletter opt-in). A builder
avoids constructors with 10 positional args and makes test data intent-revealing.

## 6. Facade (optional extension point)

A `CheckoutFacade` could wrap "add to cart → go to cart → place order → pay" into one call for
tests that don't care about the intermediate steps — only used where a scenario needs to skip
past setup steps quickly. Mentioned here as a natural next extension.

## Why separate frameworks instead of one hybrid?

A hybrid (BDD + data-driven + keyword) framework is possible and is a natural "if I had more time"
answer in interviews, but keeping them separate here makes each framework's architecture legible
on its own — useful when a reviewer opens the repo cold.
