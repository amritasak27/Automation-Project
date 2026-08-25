from pages.base_page import BasePage


class AccountInfoPage(BasePage):
    GENDER_MR = "#id_gender1"
    GENDER_MRS = "#id_gender2"
    PASSWORD_INPUT = "#password"
    DOB_DAY = "#days"
    DOB_MONTH = "#months"
    DOB_YEAR = "#years"

    FIRST_NAME = "input[data-qa='first_name']"
    LAST_NAME = "input[data-qa='last_name']"
    ADDRESS1 = "input[data-qa='address']"
    STATE = "input[data-qa='state']"
    CITY = "input[data-qa='city']"
    ZIPCODE = "input[data-qa='zipcode']"
    MOBILE_NUMBER = "input[data-qa='mobile_number']"
    CREATE_ACCOUNT_BUTTON = "button[data-qa='create-account']"

    ACCOUNT_CREATED_TITLE = "h2:has-text('Account Created!')"

    def fill_and_submit(self, title: str = "Mr"):
        gender_locator = self.GENDER_MR if title == "Mr" else self.GENDER_MRS
        self.click(gender_locator)

        self.fill(self.PASSWORD_INPUT, "ValidPass123")
        self.page.locator(self.DOB_DAY).select_option("10")
        self.page.locator(self.DOB_MONTH).select_option("5")
        self.page.locator(self.DOB_YEAR).select_option("1995")

        self.fill(self.FIRST_NAME, "Jane")
        self.fill(self.LAST_NAME, "Doe")
        self.fill(self.ADDRESS1, "123 Test Street")
        self.fill(self.CITY, "Testville")
        self.fill(self.STATE, "TestState")
        self.fill(self.ZIPCODE, "12345")
        self.fill(self.MOBILE_NUMBER, "9876543210")

        self.click(self.CREATE_ACCOUNT_BUTTON)

    def is_account_created(self) -> bool:
        return self.is_visible(self.ACCOUNT_CREATED_TITLE)
