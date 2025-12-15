from playwright.sync_api import Page, Locator

class BasePage:
    """Class de base pour tous les Page Objects"""

    def __init__(self, page: Page):
        self.page = page

    # ═══════════════════════════════════════════════════════════
    # PROPERTIES: Header commun
    # ═══════════════════════════════════════════════════════════
    
    @property
    def app_logo(self) -> Locator:
        """Logo de l'application"""
        return self.page.locator(".app_logo")
    
    @property
    def burger_menu(self) -> Locator:
        """Bouton burger menu"""
        return self.page.get_by_role("button", name="Open Menu")
    
    # ═══════════════════════════════════════════════════════════
    # PROPERTIES: Liens menu burger
    # ═══════════════════════════════════════════════════════════

    @property
    def logout_link(self) -> Locator:
        """Lien de déconnexion dans le menu burger"""
        return self.page.locator("#logout_sidebar_link")
    
    @property
    def cart_link(self) -> Locator:
        """Lien vers le panier (icône panier)"""
        return self.page.locator(".shopping_cart_link")
    
    @property
    def cart_badge(self) -> Locator:
        """Badge affichant le nombre d'articles dans le panier"""
        return self.page.locator(".shopping_cart_badge")
    
    @property
    def all_items_link(self) -> Locator:
        """Lien dans le menu burger"""
        return self.page.locator("#inventory_sidebar_link")
    
    @property
    def about_link(self) -> Locator:
        """Lien 'About' dans le menu burger"""
        return self.page.locator("#about_sidebar_link")

    @property
    def reset_app_link(self) -> Locator:
        """Lien 'Reset App State' dans le menu burger"""
        return self.page.locator("#reset_sidebar_link")
    
    # ═══════════════════════════════════════════════════════════
    # PROPERTIES: Panier
    # ═══════════════════════════════════════════════════════════

    def go_to_cart(self):
        """Naviguer vers le panier"""
        self.cart_link.click()

    def get_cart_count(self) -> int:
        """Récupérer le nombre d'articles dans le panier"""
        if not self.cart_badge.is_visible():
            return 0
        return int(self.cart_badge.text_content())
    
    def is_cart_empty(self) -> bool:
        """Vérifier si le panier est vide"""
        return not self.cart_badge.is_visible()
    
    # ═══════════════════════════════════════════════════════════
    # ACTIONS: Menu burger
    # ═══════════════════════════════════════════════════════════

    def open_menu(self):
        """Ouvrir le menu burger"""
        self.burger_menu.click()

    def logout(self):
        """Se déconnecter de l'application"""
        self.burger_menu.click()
        self.logout_link.click()

    def close_menu(self):
        """Fermer le menu burger"""
        close_button = self.page.get_by_role("button", name="Close Menu")
        close_button.click()

    # ═══════════════════════════════════════════════════════════
    # ACTIONS: Vérifications communes
    # ═══════════════════════════════════════════════════════════

    def is_logo_visible(self) -> bool:
        return self.app_logo.is_visible()
    
    def go_to_all_items(self):
        """Naviguer vers tous les produits"""
        self.burger_menu.click()
        self.all_items_link.click()
    
    def reset_app_state(self):
        """Réinitialiser l'état de l'application"""
        self.burger_menu
        self.reset_app_link.click()