# TestForge - Test Automation made easy with Python

This project automates UI tests for [the-internet.herokuapp.com](https://the-internet.herokuapp.com/) and API tests for [JSONPlaceholder](https://jsonplaceholder.typicode.com/) using Python, pytest, pytest-bdd, Playwright and Allure.

Allure report showcase: https://manitsu.gitlab.io/-/TestForge/-/jobs/16594477046/artifacts/reports/allure-report-ui/index.html

Successful pipeline showcase: https://gitlab.com/MAnitsu/TestForge/-/pipelines/2862285729

---

## Project Structure

PlaywrightFramework/

├─ features/

│   ├─ api/

│   │   └─ *.feature

│   └─ ui/

│       └─ *.feature

├─ tests/

│   ├─ api/

│   │   ├─ conftest.py

│   │   └─ test_*.py

│   └─ ui/

│       ├─ pages/

│       │   └─ *_page.py

│       ├─ data/

│       │   └─ textfile.txt

│       ├─ constants/

│       │   └─ credentials.py

│       └─ test_*.py

├─ conftest.py

├─ requirements.txt

├─ .env.example

├─ .gitignore

└─ README.md

- `features/api/` → Contains API BDD feature files
- `features/ui/` → Contains UI BDD feature files
- `tests/api/` → Contains API BDD test implementations with step definitions
- `tests/ui/` → Contains UI BDD test implementations with step definitions
- `tests/ui/pages/` → UI-related page objects
- `tests/ui/data/` → UI-related test data
- `tests/ui/constants/` → UI-related credentials
- `conftest.py` → Defines pytest fixtures for browser, page setup, API base URLs, and allure failure hooks
- `requirements.txt` → Python dependencies
- `.gitignore` → Excludes unnecessary or system-specific files from version control
- `README.md` → Documentation

---

## Prerequisites
- Python ≥ 3.9
- Git
- Playwright CLI (`pip install playwright`)

---

## Environment Variables

| Variable | Default | Description |
|---|---:|---|
| `BASE_URL` | `https://the-internet.herokuapp.com` | UI test base URL |
| `API_BASE_URL` | `https://jsonplaceholder.typicode.com` | API test base URL |
| `VALID_USER` | `tomsmith` | Valid login username |
| `VALID_PASS` | `SuperSecretPassword!` | Valid login password |
| `INVALID_USER` | `wronguser` | Invalid login username |
| `INVALID_PASS` | `wrongpassword` | Invalid login password |

The `.env` file is ignored by Git. Set these variables in `.env` locally or in CI/CD.

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
venv/Scripts/activate # activates environment

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

---

## Running Tests

Run all tests:
```bash
pytest
```

Run API tests only:
```bash
pytest tests/api
```

Run UI tests only:
```bash
pytest tests/ui
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

### API Feature Files (`features/api/`)
BDD API scenarios use the same pattern:
```gherkin
Feature: Posts API
  Scenario: Retrieve a post by id
    Given the API base URL is configured
    When I request post with id 1
    Then the response status should be 200
    And the response should contain post id 1
```

### API Test Files (`tests/api/`)
BDD API test implementations use `requests` and the same decorators:
```python
@scenario("../../features/api/posts.feature", "Retrieve a post by id")
@allure.feature("API")
@allure.story("Posts")
def test_retrieve_post():
    """Verify a post can be retrieved from the dummy API endpoint."""

@given("the API base URL is configured")
def configure_api_base_url(api_base_url):
    assert api_base_url

@when("I request post with id 1")
def request_post(api_response):
    assert api_response.status_code == 200

@then("the response should contain post id 1")
def verify_response_post_id(api_response):
    assert api_response.json()["id"] == 1
```

---

## How to Create New Tests

1. Create a feature file in `features/ui/` or `features/api/`
2. Create a test file in `tests/ui/` or `tests/api/` with `@scenario` decorators
3. Implement step definitions using `@given`, `@when`, `@then` decorators
4. Use page objects from `tests/ui/pages/` for UI interactions
5. Use `requests` fixtures from `tests/api/conftest.py` for API interactions
6. Keep explicit `@allure.feature`, `@allure.story`, and `@allure.severity` decorators for reporting

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
- Add BDD-style API tests
- Integrate tests inside CI/CD pipelines
- Run tests in headless mode for speed

### To do
- Use pytest parametrise to test multiple inputs
- Test on multiple browsers (Chromium, Firefox, WebKit)

---

## Author
Mihai A. Nițu

GitLab: https://gitlab.com/MAnitsu
LinkedIn: https://www.linkedin.com/in/mihai-alexandru-nitu-b8035a16a/
