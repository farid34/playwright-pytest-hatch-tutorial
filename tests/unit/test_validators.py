"""
Tests unitaires pour le module validators
"""
import pytest
from tutorial_tests.utils.validators import (
    validate_email,
    validate_password_strength,
    calculate_discount,
    format_username
)

# ═══════════════════════════════════════════════════════════
# TESTS: validate_email
# ═══════════════════════════════════════════════════════════

def test_validate_email_valid():
    """Test: Email valide"""
    assert validate_email("test@example.com") is True
    assert validate_email("user.name@domain.co.uk") is True

def test_validate_email_invalid_no_at():
    """Test: Email sans @"""
    assert validate_email("invalidemail.com") is False

def test_validate_email_invalid_no_dot():
    """Test: Email sans point dans le domaine"""
    assert validate_email("test@domain") is False

def test_validate_email_empty():
    """Test: Email vide"""
    assert validate_email("") is False

def test_validate_email_none():
    """Test: Email None"""
    assert validate_email(None) is False

# ═══════════════════════════════════════════════════════════
# TESTS: validate_password_strength
# ═══════════════════════════════════════════════════════════

def test_password_strength_weak():
    """Test: Mot de passe faible"""
    assert validate_password_strength("abc") == "weak"
    assert validate_password_strength("12345") == "weak"

def test_password_strength_medium():
    """Test: Mot de passe moyen"""
    assert validate_password_strength("Abc123") == "medium"
    assert validate_password_strength("Password1") == "medium"

def test_password_strength_strong():
    """Test: Mot de passe fort"""
    assert validate_password_strength("Abc123!@#") == "strong"
    assert validate_password_strength("MyP@ssw0rd!") == "strong"

def test_password_strength_empty():
    """Test: Mot de passe vide"""
    assert validate_password_strength("") == "weak"

# ═══════════════════════════════════════════════════════════
# TESTS: calculate_discount
# ═══════════════════════════════════════════════════════════

def test_calculate_discount_10_percent():
    """Test: Réduction de 10%"""
    assert calculate_discount(100, 10) == 90.0

def test_calculate_discount_50_percent():
    """Test: Réduction de 50%"""
    assert calculate_discount(100, 50) == 50.0

def test_calculate_discount_no_discount():
    """Test: Pas de réduction"""
    assert calculate_discount(100, 0) == 100.0

def test_calculate_discount_negative_price():
    """Test: Prix négatif lève une erreur"""
    with pytest.raises(ValueError, match="Price cannot be negative"):
        calculate_discount(-10, 10)

def test_calculate_discount_invalid_percent():
    """Test: Pourcentage invalide lève une erreur"""
    with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
        calculate_discount(100, 150)

# ═══════════════════════════════════════════════════════════
# TESTS: format_username
# ═══════════════════════════════════════════════════════════

def test_format_username_with_spaces():
    """Test: Username avec espaces"""
    assert format_username("  JohnDoe  ") == "johndoe"

def test_format_username_uppercase():
    """Test: Username en majuscules"""
    assert format_username("ADMIN") == "admin"

def test_format_username_mixed_case():
    """Test: Username en casse mixte"""
    assert format_username("JohnDoe123") == "johndoe123"

def test_format_username_empty():
    """Test: Username vide"""
    assert format_username("") == ""