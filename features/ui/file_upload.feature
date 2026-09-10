Feature: File Upload
  Scenario: Upload a File
    Given I navigate to the file upload page
    When I upload the file "tests/ui/data/textfile.txt"
    Then the file should be listed as uploaded
