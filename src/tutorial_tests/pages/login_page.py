"""
Page Object Model pour la page de login de Saucedemo
"""
from playwright.sync_api import Page
from rich.console import Console

console = Console()

class LoginPage:
    """
    Page de login de Saucedemo
    """

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.url = base_url

        # Locators
        self.username_input = self.page.get_by_placeholder("Username")
        self.password_input = self.page.get_by_placeholder("Password")
        self.login_button = self.page.locator("#login-button")
        self.error_message = self.page.locator("[data-test='error']")

        self.app_logo = self.page.locator(".app_logo")

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

    