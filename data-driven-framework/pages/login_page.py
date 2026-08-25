from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = "input[data-qa='login-email']"
    PASSWORD_INPUT = "input[data-qa='login-password']"
    LOGIN_BUTTON = "button[data-qa='login-button']"
    ERROR_MESSAGE = "p:has-text('Your email or password is incorrect!')"
    LOGGED_IN_INDICATOR = "a:has-text('Logged in as')"

    def login(self, email: str, password: str):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def is_login_error_visible(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)

    def is_logged_in(self) -> bool:
        return self.is_visible(self.LOGGED_IN_INDICATOR)
