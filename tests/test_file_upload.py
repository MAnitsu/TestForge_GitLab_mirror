# tests/test_file_upload.py

import allure
from pages.file_upload_page import FileUploadPage

@allure.feature("File Upload")
@allure.story("Upload a File")
@allure.severity(allure.severity_level.NORMAL)
def test_file_upload(page):
    file_upload_page = FileUploadPage(page)
    file_upload_page.navigate()

    with allure.step("Upload the file named \"textfile.txt\""):
        file_upload_page.upload_file("data/textfile.txt")

    with allure.step("Check if the correct file was updated"):
        assert file_upload_page.check_file_name("data/textfile.txt") is True