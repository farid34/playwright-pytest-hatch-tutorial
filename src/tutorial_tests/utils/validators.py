"""
Docstring for tutorial_tests.utils
Module de validation pour les tests unitaires
"""

def validate_email(email: str) -> bool:
    if not email or not isinstance(email, str):
        return False
    return "@" in email and "." in email.split("@")[-1]

def validate_password_strength(password: str) -> str:
    if not password or len(password) < 6:
        return "weak"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    strength_score = sum([has_upper, has_lower, has_digit, has_special])
    
    if strength_score >= 4 and len(password) >= 8:
        return "strong"
    elif strength_score >= 2:
        return "medium"
    else:
        return "weak"
    

def calculate_discount(price: float, discount_percent: float) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative")
    
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    
    return price * (1 - discount_percent / 100)


def format_username(username: str) -> str:
    if not username:
        return ""
    return username.strip().lower()