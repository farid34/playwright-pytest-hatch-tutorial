import pytest
from playwright.sync_api import Page

def test_saucedemo_homepage(page: Page):
    page.goto("https://www.saucedemo.com")

    assert page.locator("#login-button").is_visible()

    assert "Swag Labs" in page.title()

    print("Page SauceDemo chargée correctement")