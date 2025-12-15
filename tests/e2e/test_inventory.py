import pytest
from playwright.sync_api import expect

# ═══════════════════════════════════════════════════════════
# TESTS: Navigation et affichage
# ═══════════════════════════════════════════════════════════

@pytest.mark.smoke
def test_inventory_page_loads(login_page, inventory_page):
    """Test: La page inventory charge correctement après login"""
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_on_inventory_page()
    assert inventory_page.get_title() == "Products"
