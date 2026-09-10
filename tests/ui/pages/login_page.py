# tests/ui/pages/login_page.py

import os
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url or os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.locator("button[type='submit']")
        self.flash_success = page.locator("#flash.success")
        self.flash_error = page.locator("#flash.error")

    def navigate(self):
        self.page.goto(f"{self.base_url}/login")

    def enter_credentials(self, user: str, pwd: str):
        """Fill the username and password fields without submitting."""
        self.username.fill(user)
        self.password.fill(pwd)

    def login(self, user: str, pwd: str):
        """Enter credentials and submit the form."""
        self.enter_credentials(user, pwd)
        self.login_button.click()

    def success_message_visible(self) -> bool:
        return self.flash_success.is_visible()

    def error_message_visible(self) -> bool:
        return self.flash_error.is_visible()
