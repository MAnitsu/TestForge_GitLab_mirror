"""Dropdown feature tests."""

import allure
from pytest_bdd import given, scenario, then, when
from tests.ui.pages.dropdown_page import DropdownPage


@scenario("../../features/ui/dropdown.feature", "Select Option from Dropdown")
@allure.feature("Dropdowns")
@allure.story("Select Option from Dropdown")
@allure.severity(allure.severity_level.NORMAL)
def test_select_option():
    """Verify an option can be selected from the dropdown."""


@given("I navigate to the dropdown page")
def navigate_to_dropdown_page(page, base_url):
    """Open the dropdown page."""
    page.dropdown_page = DropdownPage(page, base_url)
    page.dropdown_page.navigate()


@when('I select option "2" from the dropdown')
def select_option_2(page):
    """Select option 2 from the dropdown."""
    page.dropdown_page.select_option("2")


@then('the option "2" should be selected')
def verify_option_2_selected(page):
    """Verify option 2 is selected."""
    assert page.dropdown_page.check_option("2") is True
