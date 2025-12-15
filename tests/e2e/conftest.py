"""
Configuration Pytest pour les tests E2E avec Playwright
"""
import os
import time
import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from datetime import datetime
from rich.console import Console

console = Console()

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
# HOOK 1: Screenshot en cas d'échec
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
        # Vérifier qu'on a une page
        if "page" in item.funcargs:
            page = item.funcargs["page"]

            # Nom du screenshot
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"tests-results/screenshots/FAILED_{item.name}_{timestamp}.png"

            # Prendre le screenshot
            page.screenshot(path=screenshot_path, full_page=True)
            console.print(f"[red]📸 Screenshot:[/red] {screenshot_path}")


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


# ==============================================
# FIXTURE: Authenticated Context (storage_state)
# ==============================================

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
# FIXTURE: Authenticated Context (storage_state)
# ═══════════════════════════════════════════════════════════

@pytest.fixture(scope="session")
def authenticated_context(browser: Browser, base_url: str):
    """
    Crée un contexte authentifié et sauvegarde le storage_state
    """
    from pathlib import Path
    from tutorial_tests.pages.login_page import LoginPage
    
    console.print("[cyan]🔐 Création de la session authentifiée...[/cyan]")
    
    # Utilisateur par défaut
    username = "standard_user"
    password = "secret_sauce"
    
    # Chemin du fichier storage_state
    storage_state_path = Path(f"playwright/.auth/storage_state_{username}.json")
    storage_state_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Si le fichier existe déjà, le réutiliser
    if storage_state_path.exists():
        console.print(f"[green]✅ Session '{username}' existante trouvée[/green]")
        return str(storage_state_path)
    
    # Sinon, créer une nouvelle session
    console.print(f"[yellow]🔑 Connexion avec '{username}'...[/yellow]")
    
    # Créer un nouveau contexte
    context = browser.new_context()
    page = context.new_page()
    
    # Utiliser LoginPage pour se connecter (réutilisation !)
    login_page = LoginPage(page, base_url)
    login_page.navigate()
    login_page.login(username, password)
    
    # Attendre que la page inventory charge
    page.wait_for_url("**/inventory.html")
    console.print("[green]✅ Connexion réussie ![/green]")
    
    # Sauvegarder le storage_state
    context.storage_state(path=str(storage_state_path))
    console.print(f"[green]✅ Session sauvegardée: {storage_state_path}[/green]")
    
    # Nettoyer
    context.close()
    
    return str(storage_state_path)

# ═══════════════════════════════════════════════════════════
# FIXTURE: Context avec storage_state
# ═══════════════════════════════════════════════════════════

@pytest.fixture
def context(browser: Browser, authenticated_context: str):
    """
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
        storage_state=authenticated_context  # ← Charge la session !
    )
    
    yield context
    
    context.close()

# ========================================
# FIXTURE: Page Playwright
# ========================================

@pytest.fixture
def page(page: Page):
    """
    Page Playwright avec logs
    avec gestion automatique des events
    """
    console.print("[cyan] Nouvelle page ouverte[/cyan]")

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
    console_errors = []
    def handle_console(msg):
        if msg.type == "error":
            # Filtrer les erreurs 401 (non critiques)
            if "401" not in msg.text:
                console_errors.append(msg.text)
                console.print(f"[red] Console Error: {msg.text}[/red]")
    page.on("console", handle_console)

    # ========================================
    # EVENT 3: Exceptions JS
    # ========================================
    page_errors = []
    def handle_page_error(error):
        page_errors.append(str(error))
        console.print(f"[red] Page Error: {error}[/red]")
    page.on("pageerror", handle_page_error)

    yield page

    # Rapport final
    total_errors = len(console_errors) + len(page_errors)
    if total_errors > 0:
        console.print(f"[yellow] {total_errors} erreur(s) JS détectée(s)[/yellow]")
    console.print("[cyan] Page fermée[/cyan]")


# ========================================
# FIXTURE: LoginPage
# ========================================

@pytest.fixture
def login_page(page, base_url):
    """
    Retourne une instance de LoginPage
    """
    from tutorial_tests.pages.login_page import LoginPage
    return LoginPage(page, base_url)

# ========================================
# FIXTURE: InventoryPage
# ========================================

@pytest.fixture
def inventory_page(page):
    """
    Retourne une instance InventoryPage
    """
    from tutorial_tests.pages.inventory_page import InventoryPage
    return InventoryPage(page)