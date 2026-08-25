from pytest_bdd import scenarios, given, when, then, parsers

from pages.home_page import HomePage
from pages.cart_page import CartPage

scenarios("../features/cart_checkout.feature")


@given("I am on the home page", target_fixture="home_page")
def go_to_home_page(page):
    home_page = HomePage(page)
    home_page.open("/")
    return home_page


@when(parsers.parse('I add "{product_name}" to the cart'))
def add_product(home_page, product_name):
    home_page.add_product_to_cart(product_name)


@when("I go to my cart", target_fixture="cart_page")
def go_to_cart(home_page, page):
    home_page.go_to_cart()
    return CartPage(page)


@then(parsers.parse('"{product_name}" should be in my cart'))
def assert_product_in_cart(cart_page, product_name):
    assert cart_page.is_product_in_cart(product_name)
