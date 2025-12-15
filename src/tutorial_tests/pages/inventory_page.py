"""
Docstring for tutorial_tests.pages.inventory_page
Page Object Model pour la page Inventory (liste des produits)
"""

from playwright.sync_api import Page, Locator
from .base_page import BasePage

class InventoryPage(BasePage):
    """Page d'inventaire des produits Saucedemo"""

    def __init__(self, page: Page):
        super().__init__(page)

    # ═══════════════════════════════════════════════════════════
    # PROPERTIES: Spécifiques à Inventory
    # ═══════════════════════════════════════════════════════════

    @property
    def title(self) -> Locator:
        """Titre de la page produits"""
        return self.page.locator(".title")
    
    @property
    def product_items(self) -> Locator:
        """Tous les produits affichés sur la page"""
        return self.page.locator(".inventory_item")
    
    @property
    def product_names(self) -> Locator:
        """Noms de tous les produits affichés sur la page"""
        return self.page.locator(".inventory_item_name")
    
    @property
    def product_prices(self) -> Locator:
        """Prix de tous les produits affichés sur la page"""
        return self.page.locator(".inventory_item_price")
    
    @property
    def add_to_cart_buttons(self) -> Locator:
        """Ajouter des articles dans le panier"""
        return self.page.get_by_role("button", name="Add to cart")
    
    @property
    def remove_cart_buttons(self) -> Locator:
        """Retirer de articles du panier"""
        return self.page.get_by_role("button", name="Remove")


    # ═══════════════════════════════════════════════════════════
    # ACTIONS: Navigation
    # ═══════════════════════════════════════════════════════════

    def get_title(self) -> str:
        """Récupérer le titre de la page"""
        return self.title.text_content()
    
    def is_on_inventory_page(self) -> bool:
        """Vérifier qu'on est bien sur la page inventory"""
        return self.title.is_visible() and self.get_title() == "Products"

    # ═══════════════════════════════════════════════════════════
    # ACTIONS: Produits
    # ═══════════════════════════════════════════════════════════

    def get_products_count(self) -> int:
        """Récupérer le nombre de produits affichés"""
        return self.product_items.count()
    
    def get_product_names(self) -> list[str]:
        """Récupérer les noms de tous les produits"""
        return [name.text_content() for name in self.product_names.all()]
    
    def get_product_prices(self) -> list[str]:
        """Récupérer les prix de tous les produits"""
        return [price.text_content() for price in self.product_prices.all()]
    

    # ═══════════════════════════════════════════════════════════
    # ACTIONS: Panier (spécifiques à Inventory)
    # ═══════════════════════════════════════════════════════════

    def add_first_product_to_cart(self):
        """Ajouter le premier produit au panier"""
        self.add_to_cart_buttons.first.click()

    def add_product_to_cart_by_index(self, index: int):
        """Ajouter un produit au panier par son index"""
        self.add_to_cart_buttons.nth(index).click()

    def add_product_to_cart_by_name(self, product_name: str):
        """Ajouter un produit au panier par son nom"""
        product_id = product_name.lower().replace(" ", "-")
        add_button = self.page.locator(f"#add-to-cart-{product_id}")
        add_button.click()

    def remove_first_product_from_cart(self):
        """Retirer le premier produit du panier"""
        self.remove_cart_buttons.first.click()