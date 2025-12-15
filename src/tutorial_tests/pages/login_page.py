"""
Page Object Model pour la page de login de Saucedemo
"""
from playwright.sync_api import Page, Locator
from .base_page import BasePage
from rich.console import Console

console = Console()

class LoginPage(BasePage):
    """
    Page de login de Saucedemo
    """

    def __init__(self, page: Page, base_url: str):
        super().__init__(page)
        self.url = base_url

    # ═══════════════════════════════════════════════════════════
    # PROPERTIES: Locators
    # ═══════════════════════════════════════════════════════════

    @property
    def username_input(self) -> Locator:
        """Champs username"""
        return self.page.get_by_placeholder("Username")
    
    @property
    def password_input(self) -> Locator:
        return self.page.get_by_placeholder("Password")
        
    @property
    def login_button(self) -> Locator:
        return self.page.locator("#login-button")
    
    @property
    def error_message(self) -> Locator:
        return self.page.locator("[data-test='error']")

    # ═══════════════════════════════════════════════════════════
    # ACTIONS
    # ═══════════════════════════════════════════════════════════

    def navigate(self):
        """
        Naviguer vers la page 
        """
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        """ Se connecter """
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        """
        Récupérer le message d'erreur
        """
        return self.error_message.text_content()
    
    def is_error_displayed(self):
        """
        Vérifier si un message d'erreur est affiché
        """
        return self.error_message.is_visible()

    