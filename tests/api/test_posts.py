"""Posts API feature tests."""

import allure
from pytest_bdd import given, scenario, then, when


@scenario("../../features/api/posts.feature", "Retrieve a post by id")
@allure.feature("API")
@allure.story("Posts")
@allure.severity(allure.severity_level.NORMAL)
def test_retrieve_post():
    """Verify a post can be retrieved from the dummy API endpoint."""


@given("the API base URL is configured")
def configure_api_base_url(api_base_url):
    """Ensure the API base URL is available."""
    assert api_base_url


@when("I request post with id 1")
def request_post(api_response):
    """Request the post from the dummy API endpoint."""
    assert api_response.status_code == 200


@then("the response status should be 200")
def verify_response_status(api_response):
    """Verify the HTTP response is successful."""
    assert api_response.status_code == 200


@then("the response should contain post id 1")
def verify_response_post_id(api_response):
    """Verify the returned post has the expected id."""
    assert api_response.json()["id"] == 1
