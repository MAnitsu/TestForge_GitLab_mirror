# tests/ui/pages/dynamic_loading_page.py

import os
from playwright.sync_api import Page


class DynamicLoadingPage:
    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url or os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
        self.start_button = page.locator("#start button")
        self.finish_locator = page.locator("#finish")

    def navigate(self):
        self.page.goto(f"{self.base_url}/dynamic_loading/2")

    def click_start(self):
        self.start_button.click()

    def wait_loading(self, miliseconds):
        self.finish_locator.wait_for(timeout=miliseconds)

    def check_message(self, expected_message: str) -> bool:
        return self.finish_locator.inner_text() == expected_message
