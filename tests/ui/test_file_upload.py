"""File Upload feature tests."""

import allure
from pytest_bdd import given, scenario, then, when
from tests.ui.pages.file_upload_page import FileUploadPage


@scenario("../../features/ui/file_upload.feature", "Upload a File")
@allure.feature("File Upload")
@allure.story("Upload a File")
@allure.severity(allure.severity_level.NORMAL)
def test_upload_file():
    """Verify a file can be uploaded."""


@given("I navigate to the file upload page")
def navigate_to_file_upload_page(page, base_url):
    """Open the file upload page."""
    page.file_upload_page = FileUploadPage(page, base_url)
    page.file_upload_page.navigate()


@when('I upload the file "tests/ui/data/textfile.txt"')
def upload_file(page):
    """Upload the test file."""
    page.file_upload_page.upload_file("tests/ui/data/textfile.txt")


@then("the file should be listed as uploaded")
def verify_file_uploaded(page):
    """Verify the uploaded file is listed."""
    assert page.file_upload_page.check_file_name("data/textfile.txt") is True
