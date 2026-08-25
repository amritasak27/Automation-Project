from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ROWS = "#cart_info_table tbody tr"
    PROCEED_TO_CHECKOUT = "a:has-text('Proceed To Checkout')"

    def product_row(self, product_name: str) -> str:
        return f"{self.CART_ROWS}:has-text('{product_name}')"

    def is_product_in_cart(self, product_name: str) -> bool:
        return self.is_visible(self.product_row(product_name))

    def proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT)
