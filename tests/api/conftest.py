# tests/api/conftest.py
import os
from dotenv import load_dotenv
import requests
import pytest

load_dotenv()


@pytest.fixture(scope="session")
def api_base_url():
    return os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com").rstrip("/")


@pytest.fixture
def api_response(api_base_url):
    return requests.get(f"{api_base_url}/posts/1", timeout=15)
