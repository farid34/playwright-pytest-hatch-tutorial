"""
Configuration Pytest pour les tests E2E avec Playwright
"""
import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from datetime import datetime
from rich.console import Console

console = Console()

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
    return {
        "headless": False, # Voir le navigateur
        "slow_mo": 300, # Ralentir de 300 ms
    }

# ========================================
# FIXTURE: URL de base
# ========================================

@pytest.fixture(scope="session")
def base_url():
    """
    URL du site à tester
    """
    return "https://www.saucedemo.com"

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