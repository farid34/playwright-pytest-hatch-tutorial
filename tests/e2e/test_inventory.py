import pytest
from playwright.sync_api import expect

# ═══════════════════════════════════════════════════════════
# TESTS: Navigation et affichage
# ═══════════════════════════════════════════════════════════

@pytest.mark.smoke
def test_inventory_page_loads(inventory_page):
    """Test: La page inventory charge correctement après login"""
    inventory_page.navigate()

    assert inventory_page.is_on_inventory_page()
    assert inventory_page.get_title() == "Products"
