from pages.base_page import BasePage


class SignupPage(BasePage):
    NAME_INPUT = "input[data-qa='signup-name']"
    EMAIL_INPUT = "input[data-qa='signup-email']"
    SIGNUP_BUTTON = "button[data-qa='signup-button']"
    ACCOUNT_INFO_TITLE = "h2:has-text('Enter Account Information')"
    EMAIL_EXISTS_ERROR = "p:has-text('Email Address already exist!')"

    def start_signup(self, name: str, email: str):
        self.fill(self.NAME_INPUT, name)
        self.fill(self.EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)

    def is_account_info_form_visible(self) -> bool:
        return self.is_visible(self.ACCOUNT_INFO_TITLE)

    def is_email_exists_error_visible(self) -> bool:
        return self.is_visible(self.EMAIL_EXISTS_ERROR)
