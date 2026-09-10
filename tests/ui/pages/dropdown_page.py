# tests/ui/pages/dropdown_page.py

import os
from playwright.sync_api import Page


class DropdownPage:
    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url or os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
        self.dropdown = page.locator("#dropdown")

    def navigate(self):
        self.page.goto(f"{self.base_url}/dropdown")

    def select_option(self, option: str):
        self.dropdown.select_option(option)

    def check_option(self, option: str) -> bool:
        return self.dropdown.input_value() == option
