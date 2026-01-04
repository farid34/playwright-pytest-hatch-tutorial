import pytest
from playwright.sync_api import Playwright, APIRequestContext
from dotenv import load_dotenv
from pathlib import Path

# Charger .env depuis la racine du projet
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

from creds import *


@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    context = playwright.request.new_context(
        base_url="https://api.github.com",
        extra_http_headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}"
        }   
    )
    yield context
    context.dispose()


@pytest.fixture(autouse=True, scope="session")
def create_test_repository(api_context: APIRequestContext):
    post_response = api_context.post(
        "/user/repos",
        data={"name": GITHUB_REPO}
    )

    assert post_response.ok

    yield

    delete_response = api_context.delete(
        f"/repos/{GITHUB_USER}/{GITHUB_REPO}"
    )

    assert delete_response.ok