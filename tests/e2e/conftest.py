"""
Configuration Pytest pour les tests E2E avec Playwright
"""
import os
import json
import time
import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from datetime import datetime
from pathlib import Path
from rich.console import Console

console = Console()

# ========================================
# HELPER: Configuration commune des pages
# ========================================

def configure_page(page: Page) -> Page:
    """
    Configuration commune pour toutes les pages
    """
    #console.print("[cyan] Nouvelle page ouverte[/cyan]")

    # ========================================
    # BLOQUER LES RESSOURCES INUTILES
    # ========================================
    #page.route("**", lambda route: route.abort() if route.request.resource_type in ["images", "font", "stylesheet"] else route.continue_())
    #page.route("**/*.{png,jpg,jpeg,gif,svg,woff,woff2}", lambda route: route.abort())
    #page.route("**/analytics**", lambda route: route.abort())
    #page.route("**/tracking**", lambda route: route.abort())

    # ========================================
    # EVENT 1: Gérer les dialogs automatiquement
    # ========================================
    def handle_dialog(dialog):
        console.print(f"[yellow] Dialog détecté: {dialog.type} - {dialog.message}[/yellow]")
        dialog.accept() # Accepter automatiquement
    page.on("dialog", handle_dialog)

    # ========================================
    # EVENT 2: Erreurs console JS
    # ========================================
    def handle_console(msg):
        if msg.type == "error" and "401" not in msg.text:
            console.print(f"[red] Console Error: {msg.text}[/red]")
    page.on("console", handle_console)

    # ========================================
    # EVENT 3: Exceptions JS
    # ========================================
    def handle_page_error(error):
        console.print(f"[red] Page Error: {error}[/red]")
    page.on("pageerror", handle_page_error)

    return page

# ========================================
# FIXTURE: Configuration du navigateur
# ========================================

@pytest.fixture(scope="session")
def browser_type_launch_args():
    """
    Configuration du navigateur (une seule fois pour tous les tests)
    """
    # Headless si en CI, sinon visible
    is_ci = os.getenv("CI", "false") == "true"

    return {
        "headless": is_ci,
        "slow_mo": 300, # Ralentir de 300 ms
    }

"""@pytest.fixture(scope="session")
def browser_context_args():
    pytest.skip("Désactivé ici car le site a besoin de javascript")
    return {
        "java_script_enabled": False
    }"""

# ========================================
# FIXTURE: URL de base
# ========================================

@pytest.fixture(scope="session")
def base_url():
    """
    URL du site à tester
    """
    return "https://www.saucedemo.com"


# ═══════════════════════════════════════════════════════════
# FIXTURE: Storage state (authentification)
# ═══════════════════════════════════════════════════════════

@pytest.fixture(scope="session")
def storage_state_path(browser: Browser, base_url: str):
    """
    Crée un contexte authentifié et sauvegarde le storage_state
    """
    from tutorial_tests.pages.login_page import LoginPage
    
    console.print("[cyan] Création de la session authentifiée...[/cyan]")
    
    # Utilisateur par défaut
    username = "standard_user"
    password = "secret_sauce"

    # Chemin du fichier storage_state
    path = Path(f"playwright/.auth/storage_state_{username}.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Si le fichier existe déjà, le réutiliser
    if path.exists():
        with open(path) as f:
            data = json.load(f)
        
        for cookie in data.get("cookies", []):
            if cookie.get("expires", 0) < time.time():
                console.print(f"[yellow]⚠️ Storage state expiré, régénération...[/yellow]")
                break
        else:
            # Aucun cookie expiré, on réutilise
            console.print(f"[green]✅ Storage state existant avec '{username}': {path}[/green]")
            return str(path)
    
    # Sinon, créer une nouvelle session
    console.print(f"[yellow] Création du storage state avec '{username}'...[/yellow]")
    
    # Créer un nouveau contexte
    context = browser.new_context()
    page = context.new_page()
    
    # Utiliser LoginPage pour se connecter (réutilisation !)
    login_page = LoginPage(page, base_url)
    login_page.navigate()
    login_page.login(username, password)
    
    # Attendre que la page inventory charge
    page.wait_for_url("**/inventory.html")
    console.print(f"[green]✅ Connexion réussie avec storage state: '{path}'![/green]")
    
    # Sauvegarder le storage_state
    context.storage_state(path=str(path))
    console.print(f"[green]✅ Session sauvegardée: {path}[/green]")
    
    # Nettoyer
    context.close()
    
    return str(path)

# ═══════════════════════════════════════════════════════════
# FIXTURE: Page sans authentification (pour tests login)
# ═══════════════════════════════════════════════════════════

@pytest.fixture
def page(browser: Browser):
    """
    Page sans authentification
    Utiliser pour les tests de login
    """
    context = browser.new_context()
    page = context.new_page()
    configure_page(page)

    console.print("[cyan]📄 Page créée (sans auth)[/cyan]")
    
    yield page
    
    context.close()
    console.print("[cyan]📄 Page fermée[/cyan]")

# ═══════════════════════════════════════════════════════════
# FIXTURE: Page avec authentification (pour la majorité des tests)
# ═══════════════════════════════════════════════════════════

@pytest.fixture
def authenticated_page(browser: Browser, storage_state_path: str):
    """
    Page avec authentification pré-chargée.
    Chaque test a son propre context (isolation)

    Contexte Playwright avec storage_state (authentification persistante)
    Charge automatiquement le storage_state créé par authenticated_context
    
    Args:
        browser: Instance Playwright Browser
        authenticated_context: Chemin vers storage_state.json
        
    Returns:
        BrowserContext: Contexte avec authentification
    """
    # Créer un contexte avec le storage_state
    context = browser.new_context(
        storage_state=storage_state_path  # ← Charge la session !
    )
    
    page = context.new_page()
    configure_page(page)
    
    console.print("[cyan]📄 Page créée (authentifiée)[/cyan]")
    
    yield page

    context.close()
    console.print("[cyan]📄 Page fermée[/cyan]")


# ========================================
# FIXTURE: LoginPage
# ========================================

@pytest.fixture
def login_page(page: Page, base_url: str):
    """
    Retourne une instance de LoginPage
    """
    from tutorial_tests.pages.login_page import LoginPage
    return LoginPage(page, base_url)

# ========================================
# FIXTURE: InventoryPage
# ========================================

@pytest.fixture
def inventory_page(authenticated_page: Page, base_url: str):
    """
    Retourne une instance InventoryPage
    """
    from tutorial_tests.pages.inventory_page import InventoryPage
    return InventoryPage(authenticated_page, base_url)

# ═══════════════════════════════════════════════════════════
# FIXTURE AUTOUSE: Mesure du temps
# ═══════════════════════════════════════════════════════════

@pytest.fixture(autouse=True)
def measure_test_time(request):
    """Mesure le temps de chaque test automatiquement"""
    start_time = time.time()
    test_name = request.node.name
    console.print(f"[blue]⏱️  Démarrage:[/blue] {test_name}")
    
    yield
    
    duration = time.time() - start_time
    console.print(f"[blue]⏱️  Durée:[/blue] {duration:.2f}s")


# ========================================
# HOOK: Screenshot en cas d'échec
# ========================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Exécuté après chaque test
    Prend un screenshot si le test échoue
    """
    outcome = yield
    report = outcome.get_result()

    # Si le test a échoué
    if report.when == "call" and report.failed:
        # Verifier qu'on a une page authentifié (storage state)
        if "authenticated_page" in item.funcargs:
            page = item.funcargs["authenticated_page"]
        # Sinon vérifier qu'on a une simple page sans authentification
        elif "page" in item.funcargs:
            page = item.funcargs["page"]

        # Nom du screenshot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"tests-results/screenshots/FAILED_{item.name}_{timestamp}.png"

        # Prendre le screenshot
        page.screenshot(path=screenshot_path, full_page=True)
        console.print(f"[red]📸 Screenshot:[/red] {screenshot_path}")