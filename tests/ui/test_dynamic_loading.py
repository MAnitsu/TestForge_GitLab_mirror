"""Dynamic Loading feature tests."""

import allure
from pytest_bdd import given, scenario, then, when
from tests.ui.pages.dynamic_loading_page import DynamicLoadingPage


@scenario("../../features/ui/dynamic_loading.feature", "Load Hidden Element")
@allure.feature("Dynamic Loading")
@allure.story("Load Hidden Element")
@allure.severity(allure.severity_level.NORMAL)
def test_load_hidden_element():
    """Verify hidden elements load correctly."""


@given("I navigate to the dynamic loading page")
def navigate_to_dynamic_loading_page(page, base_url):
    """Open the dynamic loading page."""
    page.dynamic_loading_page = DynamicLoadingPage(page, base_url)
    page.dynamic_loading_page.navigate()


@when("I click the start button")
def click_start_button(page):
    """Click the start button to begin loading."""
    page.dynamic_loading_page.click_start()


@when("I wait for the loading to complete")
def wait_for_loading(page):
    """Wait for the loading to complete."""
    page.dynamic_loading_page.wait_loading(6000)


@then("I should see the final message")
def verify_final_message(page):
    """Verify the final message is displayed."""
    assert page.dynamic_loading_page.check_message("Hello World!") is True
