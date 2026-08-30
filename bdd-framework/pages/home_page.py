from pages.base_page import BasePage


class HomePage(BasePage):
    def product_add_to_cart_button(self, product_name: str) -> str:
        return (
            f"div.product-image-wrapper:has-text('{product_name}') "
            ".productinfo a:has-text('Add to cart')"
        )

    CONTINUE_SHOPPING_BUTTON = "button:has-text('Continue Shopping')"
    CART_LINK = "a[href='/view_cart']"

    def add_product_to_cart(self, product_name: str):
        self.click_first(self.product_add_to_cart_button(product_name))
        if self.is_visible(self.CONTINUE_SHOPPING_BUTTON):
            self.click(self.CONTINUE_SHOPPING_BUTTON)

    def go_to_cart(self):
        self.click(self.CART_LINK)