from pages.base_page import BasePage


class AccountInfoPage(BasePage):
    """The 'Enter Account Information' form shown after start_signup().
    Field data-qa/id attributes verified against the live signup form.
    """

    GENDER_MR = "#id_gender1"
    GENDER_MRS = "#id_gender2"
    PASSWORD_INPUT = "#password"
    DOB_DAY = "#days"
    DOB_MONTH = "#months"
    DOB_YEAR = "#years"
    NEWSLETTER_CHECKBOX = "#newsletter"
    OFFERS_CHECKBOX = "#optin"

    FIRST_NAME = "input[data-qa='first_name']"
    LAST_NAME = "input[data-qa='last_name']"
    COMPANY = "input[data-qa='company']"
    ADDRESS1 = "input[data-qa='address']"
    ADDRESS2 = "input[data-qa='address2']"
    COUNTRY = "select[data-qa='country']"
    STATE = "input[data-qa='state']"
    CITY = "input[data-qa='city']"
    ZIPCODE = "input[data-qa='zipcode']"
    MOBILE_NUMBER = "input[data-qa='mobile_number']"
    CREATE_ACCOUNT_BUTTON = "button[data-qa='create-account']"

    ACCOUNT_CREATED_TITLE = "h2:has-text('Account Created!')"

    def fill_account_info(self, data: dict):
        gender_locator = self.GENDER_MR if data.get("title", "Mr") == "Mr" else self.GENDER_MRS
        self.click(gender_locator)

        self.fill(self.PASSWORD_INPUT, data["password"])
        self.page.locator(self.DOB_DAY).select_option(data.get("dob_day", "10"))
        self.page.locator(self.DOB_MONTH).select_option(data.get("dob_month", "5"))
        self.page.locator(self.DOB_YEAR).select_option(data.get("dob_year", "1995"))

        self.fill(self.FIRST_NAME, data["first_name"])
        self.fill(self.LAST_NAME, data["last_name"])
        self.fill(self.ADDRESS1, data.get("address1", "123 Test Street"))
        self.fill(self.CITY, data.get("city", "Testville"))
        self.fill(self.STATE, data.get("state", "TestState"))
        self.fill(self.ZIPCODE, data["zipcode"])
        self.fill(self.MOBILE_NUMBER, data["mobile_number"])

    def submit(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def is_account_created(self) -> bool:
        return self.is_visible(self.ACCOUNT_CREATED_TITLE)
