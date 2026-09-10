# conftest.py
import os
import pytest
import allure
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from tests.ui.constants.credentials import LoginConfig

# Load environment variables from .env file if it exists
load_dotenv()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()

    page.console_messages = []
    page.network_events = []

    page.on("console", lambda msg: page.console_messages.append(f"[{msg.type}] {msg.text}"))
    page.on("request", lambda req: page.network_events.append(f"➡️ {req.method} {req.url}"))
    page.on("response", lambda res: page.network_events.append(f"⬅️ {res.status} {res.url}"))

    yield page
    context.close()


@pytest.fixture
def base_url():
    return os.getenv("BASE_URL", "https://the-internet.herokuapp.com")


@pytest.fixture
def valid_credentials():
    return LoginConfig.get_user("valid_credentials")


@pytest.fixture
def invalid_credentials():
    return LoginConfig.get_user("invalid_credentials")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot = page.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name=f"{item.name}_failure",
                attachment_type=allure.attachment_type.PNG
            )

            if page.console_messages:
                allure.attach(
                    "\n".join(page.console_messages),
                    name=f"{item.name}_console",
                    attachment_type=allure.attachment_type.TEXT
                )

            if page.network_events:
                allure.attach(
                    "\n".join(page.network_events),
                    name=f"{item.name}_network",
                    attachment_type=allure.attachment_type.TEXT
                )
