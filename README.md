# UI Test Automation with Python & Playwright

This project automates UI tests for [the-internet.herokuapp.com](https://the-internet.herokuapp.com/) using Python, pytest, pytest-bdd, Playwright and Allure.

Allure report showcase: https://manitsu.github.io/PlaywrightFramework/#

---

## Project Structure

PlaywrightFramework/

├─ features/ui/

│   └─ *.feature

├─ tests/

│   ├─ ui/

│   │   ├─ pages/

│   │   │   └─ *_page.py

│   │   ├─ data/

│   │   │   └─ textfile.txt

│   │   ├─ constants/

│   │   │   └─ credentials.py

│   │   ├─ test_*.py

├─ conftest.py

├─ requirements.txt

├─ .env

├─ .gitignore

└─ README.md

- `features/ui/` → Contains BDD feature files (Gherkin scenarios)
- `tests/ui/` → Contains BDD test implementations with step definitions
- `tests/ui/pages/` → UI-related page objects
- `tests/ui/data/` → UI-related test data
- `tests/ui/constants/` → UI-related credentials
- `conftest.py` → Defines pytest fixtures for browser, page setup, and allure failure hooks
- `requirements.txt` → Python dependencies
- `.gitignore` → Excludes unnecessary or system-specific files from version control
- `README.md` → Documentation

---

## Prerequisites
- Python ≥ 3.9
- Git
- Playwright CLI (`pip install playwright`)

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/MAnitsu/PlaywrightUITest.git
cd PlaywrightUITest
```

### 2. Create a Virtual Environment
The virtual environment is not included in the repository. Each user should generate it locally depending on their OS and activate it when running tests locally, then deactivate it after all the desired tests are done.

```bash
# Windows:
python -m venv venv
venv\Scripts\activate # activates environment

# macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```
Deactivate virtual environment:
```bash
deactivate
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers
```bash
playwright install
```

### 5. Configure BASE_URL
Copy the `.env.example` file and set your base URL:
```bash
cp .env.example .env
# Edit .env to set BASE_URL
```

Default: `https://the-internet.herokuapp.com`

---

## Running Tests

Run all tests:
```bash
pytest
```
Run a specific test file:
```bash
pytest tests/ui/test_login.py
```

Run tests with detailed output:
```bash
pytest -v
```

Run tests and generate an HTML report
```bash
pip install pytest-html
pytest --html=report.html --self-contained-html
```

Run tests with Allure Report
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## BDD Test Structure

### Feature Files (`features/ui/`)
Gherkin scenarios defining the behavior:
```gherkin
Feature: Login
  Scenario: Valid Login
    Given I navigate to the login page
    When I enter valid credentials
    And I click the login button
    Then I should see a success message
```

### Test Files (`tests/ui/`)
BDD test implementations with step definitions:
```python
@scenario("../../features/ui/login.feature", "Valid Login")
@allure.feature("Login")
@allure.story("Valid Login")
def test_valid_login():
    """Verify a user can log in with valid credentials."""

@given("I navigate to the login page")
def navigate_to_login_page(page, base_url):
    page.login_page = LoginPage(page, base_url)
    page.login_page.navigate()

@when("I enter valid credentials")
def enter_valid_credentials(page, valid_credentials):
    page.login_page.enter_credentials(...)

@when("I click the login button")
def click_login_button(page):
    page.login_page.login_button.click()

@then("I should see a success message")
def verify_success_message(page):
    assert page.login_page.success_message_visible()
```

---

## How to Create New Tests

1. Create a feature file in `features/ui/`
2. Create a test file in `tests/ui/` with `@scenario` decorators
3. Implement step definitions using `@given`, `@when`, `@then` decorators
4. Use page objects from `tests/ui/pages/` for UI interactions
5. Keep explicit `@allure.feature`, `@allure.story`, and `@allure.severity` decorators for reporting

---

## Playwright Locator Tips
Examples:
```python
page.locator("#username")
page.locator(".button")
page.locator("button[type='submit']")
```

---

## Ways to Expand This Project

### Done
- Implement the Page Object Model (POM)
- Generate HTML test reports (Allure)
- Add BDD-Style Gherkin test scenarios

### To do
- Use pytest parametrise to test multiple inputs
- Add API tests
- Integrate tests inside CI/CD pipelines
- Run tests in headless mode for speed
- Test on multiple browsers (Chromium, Firefox, WebKit)

---

## Author
Mihai A. Nițu

GitLab: https://gitlab.com/MAnitsu
LinkedIn: https://www.linkedin.com/in/mihai-alexandru-nitu-b8035a16a/
