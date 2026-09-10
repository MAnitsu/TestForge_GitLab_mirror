# tests/ui/pages/file_upload_page.py

import os
from pathlib import Path
from playwright.sync_api import Page


class FileUploadPage:
    def __init__(self, page: Page, base_url: str = ""):
        self.page = page
        self.base_url = base_url or os.getenv("BASE_URL", "")
        self.choose_file_button = page.locator("#file-upload")
        self.upload_button = page.locator("#file-submit")
        self.uploaded_text = page.locator("#uploaded-files")

    def navigate(self):
        self.page.goto(f"{self.base_url}/upload")

    def upload_file(self, filename: str):
        self.choose_file_button.set_input_files(filename)
        self.upload_button.click()

    def check_file_name(self, filename: str) -> bool:
        """Return True if the uploaded file name matches (handles paths)."""
        expected = Path(filename).name
        return self.uploaded_text.inner_text() == expected
