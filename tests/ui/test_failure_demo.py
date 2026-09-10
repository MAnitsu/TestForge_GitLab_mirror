"""Intentional failure demo for allure reporting."""

import allure


@allure.title("Intentional Failure Demo")
@allure.severity(allure.severity_level.CRITICAL)
def test_intentional_failure(page):
    """Intentional failure used to verify allure failure attachments."""
    page.goto("https://example.com")
    assert page.locator("h1").inner_text() == "Non-Existent Text"
