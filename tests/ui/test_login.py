"""Login feature tests."""

import allure
from pytest_bdd import given, scenario, then, when
from tests.ui.pages.login_page import LoginPage


@scenario("../../features/ui/login.feature", "Valid Login")
@allure.feature("Login")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login():
    """Verify a user can log in with valid credentials."""


@scenario("../../features/ui/login.feature", "Invalid Login")
@allure.feature("Login")
@allure.story("Invalid Login")
@allure.severity(allure.severity_level.NORMAL)
def test_invalid_login():
    """Verify a user cannot log in with invalid credentials."""


@given("I navigate to the login page")
def navigate_to_login_page(page, base_url):
    """Open the login page."""
    page.login_page = LoginPage(page, base_url)
    page.login_page.navigate()


@when("I enter valid credentials")
def enter_valid_credentials(page, valid_credentials):
    """Fill in the form with valid credentials."""
    page.login_page.enter_credentials(
        valid_credentials["username"],
        valid_credentials["password"],
    )


@when("I enter invalid credentials")
def enter_invalid_credentials(page, invalid_credentials):
    """Fill in the form with invalid credentials."""
    page.login_page.enter_credentials(
        invalid_credentials["username"],
        invalid_credentials["password"],
    )


@when("I click the login button")
def click_login_button(page):
    """Submit the login form."""
    page.login_page.login_button.click()


@then("I should see a success message")
def verify_success_message(page):
    """Verify the successful login message is visible."""
    assert page.login_page.success_message_visible()


@then("I should see an error message")
def verify_error_message(page):
    """Verify the error message is visible."""
    assert page.login_page.error_message_visible()
