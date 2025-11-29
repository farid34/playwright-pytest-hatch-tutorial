import pytest
from pathlib import Path
from datetime import datetime
from rich.console import Console

# Console Rich globale
console = Console()


# ========================================
# HOOK 1: Configuration au démarrage
# ========================================

def pytest_configure(config):
    """
    Hook exécuté UNE SEULE FOIS au tout début
    AVANT que les tests ne commencent
    """
    console.rule("[bold blue] DÉBUT DE LA SESSION DE TESTS")
    console.print(f"[cyan] Date:[/cyan] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    Path("tests-results/screenshots").mkdir(parents=True, exist_ok=True)
    Path("tests-results/videos").mkdir(parents=True, exist_ok=True)
    Path("tests-results/traces").mkdir(parents=True, exist_ok=True)

    console.print("[green]✅ Dossiers screenshots, videos, traces créés[/green]\n")


# ========================================
# HOOK 2: Avant chaque test
# ========================================

def pytest_runtest_setup(item):
    """Exécuté avant chaque test"""
    console.print(f"\n[yellow] Test:[/yellow] {item.name}")


# ========================================
# HOOK 3: Après chaque test
# ========================================

def pytest_runtest_teardown(item, nextitem):
    """
    Exécuté APRÈS chaque test
    """
    console.print(f"[green]✅ Terminé:[/green] {item.name}\n")


# ========================================
# HOOK 4: À la fin de tous les tests
# ========================================

def pytest_sessionfinish(session, exitstatus):
    """
    Exécuté UNE SEULE FOIS à la fin
    APRÈS tous les tests
    """
    console.rule("[bold blue] FIN DE LA SESSION")
    console.print(f"[cyan] Status:[/cyan] {exitstatus}\n")