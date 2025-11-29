"""
Tests de la page de login
"""
import pytest
from playwright.sync_api import expect

@pytest.mark.smoke
def test_login_success(login_page):
    """Test: Login avec identifiants valides"""
    # Naviguer vers la page de login
    login_page.navigate()

    # Se connecter
    login_page.login("standard_user", "secret_sauce")

    # Vérifier qu'on est redirigé vers la page inventory
    expect(login_page.app_logo).to_have_text("Swag Labs")