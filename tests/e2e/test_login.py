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


@pytest.mark.smoke
def test_login_locked_user(login_page):
    """Test: Login avec un utilisateur bloqué"""
    login_page.navigate()
    login_page.login("locked_out_user", "secret_sauce")

    assert login_page.is_error_displayed
    error_message = login_page.get_error_message()
    assert "Sorry, this user has been locked out" in error_message