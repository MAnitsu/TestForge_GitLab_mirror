"""Checkboxes feature tests."""

import allure
from pytest_bdd import given, scenario, then, when
from tests.ui.pages.checkbox_page import CheckboxPage


@scenario("../../features/ui/checkboxes.feature", "Check and Uncheck Boxes")
@allure.feature("Checkboxes")
@allure.story("Check and Uncheck Boxes")
@allure.severity(allure.severity_level.NORMAL)
def test_check_boxes():
    """Verify checkboxes can be checked and unchecked."""


@given("I navigate to the checkboxes page")
def navigate_to_checkboxes_page(page, base_url):
    """Open the checkboxes page."""
    page.checkbox_page = CheckboxPage(page, base_url)
    page.checkbox_page.navigate()


@when("I check checkbox 0")
def check_checkbox_0(page):
    """Check the first checkbox."""
    page.checkbox_page.check(0)


@when("I uncheck checkbox 1")
def uncheck_checkbox_1(page):
    """Uncheck the second checkbox."""
    page.checkbox_page.uncheck(1)


@then("checkbox 0 should be checked")
def verify_checkbox_0_checked(page):
    """Verify the first checkbox is checked."""
    assert page.checkbox_page.is_checked(0) is True


@then("checkbox 1 should be unchecked")
def verify_checkbox_1_unchecked(page):
    """Verify the second checkbox is unchecked."""
    assert page.checkbox_page.is_checked(1) is False
