# 🎭 Playwright + Pytest avec Hatch - Guide d'installation complet

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Playwright](https://img.shields.io/badge/Playwright-1.40-green?logo=playwright)
![Pytest](https://img.shields.io/badge/Pytest-7.4-orange?logo=pytest)
![Hatch](https://img.shields.io/badge/Hatch-1.9-purple)

![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat&logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)

> 📚 Documentation complète d'un projet de tests automatisés web avec Playwright, Pytest et Hatch, depuis l'installation jusqu'à la CI/CD.

**Compatible Windows et Linux** - Documentation multi-plateforme incluse

---

## 📋 Table des Matières

- [Vue d'ensemble](#-vue-densemble)
- [Prérequis](#-prérequis)
- [Étape 1 : Python](#-étape-1--installation-python-312)
- [Étape 2 : Hatch](#-étape-2--installation-hatch)
- [Étape 3 : Projet](#-étape-3--création-du-projet)
- [Étape 4 : Configuration](#-étape-4--configuration)
- [Étape 5 : Page Objects](#-étape-5--création-des-page-objects)
- [Étape 6 : Premier Test](#-étape-6--premier-test)
- [Étape 7 : CI/CD](#-étape-7--cicd-github-actions)
- [Étape 8 : Allure](#-étape-8--installation-allure-optionnel)
- [Troubleshooting](#-troubleshooting)

---

## 🎯 Vue d'ensemble

Ce projet documente l'apprentissage et la mise en place d'un framework de tests automatisés web utilisant :
- **Playwright** - Automatisation de navigateur moderne et rapide
- **Pytest** - Framework de tests Python flexible
- **Hatch** - Gestionnaire de projet Python moderne
- **GitHub Actions** - Pipeline CI/CD


### 🎨 Ce que nous allons construire
```
Python 3.12 + pip
    ↓
Hatch (gestionnaire de projet moderne)
    ↓
Playwright + Navigateurs (Chromium, Firefox, WebKit)
    ↓
Pytest + Plugins (pytest-playwright, rich, allure)
    ↓
Structure projet + Configuration (pyproject.toml, conftest.py)
    ↓
Page Object Model (LoginPage)
    ↓
Tests E2E automatisés
    ↓
CI/CD GitHub Actions
    ↓
✅ Plateforme de tests professionnelle !

---

## 📋 Prérequis

### Système requis

- **OS:** Windows 10/11 ou Linux (Ubuntu 20.04+)
- **Compte GitHub:** Pour CI/CD (optionnel)
- **Éditeur:** VS Code, PyCharm ou autre

---

## 🐍 Étape 1 : Installation Python 3.12

### 🪟 Windows

**1. Télécharger Python**

Aller sur [python.org/downloads](https://www.python.org/downloads/) et télécharger **Python 3.12.x**

**2. Installer avec les bonnes options**

⚠️ **CRITIQUE:** Cocher **"Add Python to PATH"** !

![Python PATH](https://img.shields.io/badge/⚠️_IMPORTANT-Add_Python_to_PATH-red)
```
Options à cocher:
✅ Add Python 3.12 to PATH
✅ Install for all users
✅ Include pip
```

**3. Vérifier l'installation**
```powershell
python --version
# Python 3.12.x

pip --version
# pip 24.x.x
```

✅ **Python installé avec succès !**

---

### 🐧 Linux
```bash
# Mettre à jour les paquets
sudo apt update

# Installer Python 3.12 + pip
sudo apt install python3.12 python3.12-venv python3-pip -y

# Vérifier
python3.12 --version  # Python 3.12.x
pip3 --version        # pip 24.x.x
```

✅ **Python installé avec succès !**

---

## 📦 Étape 2 : Installation Hatch

### 💡 Qu'est-ce que Hatch ?

**Hatch** est un gestionnaire de projet Python moderne qui remplace :

|    Ancien outil    |         Hatch        |          Avantage          |
|--------------------|----------------------|----------------------------|
| `venv`             | ✅ Intégré          | Environnements automatiques |
| `requirements.txt` | ✅ `pyproject.toml` | Configuration centralisée   |
| `setup.py`         | ✅ `pyproject.toml` | Un seul fichier             |
| Scripts bash       | ✅ Scripts intégrés | Cross-platform              |

---

### Installation
```bash
pip install hatch
```

**Vérification:**
```bash
hatch --version
# Hatch, version 1.9.x
```

✅ **Hatch installé avec succès !**

---

## 🔧 Étape 2.5 : Installation Git

### 🪟 Windows

**Télécharger:**
1. Aller sur [git-scm.com/downloads](https://git-scm.com/downloads)
2. Télécharger Git pour Windows
3. Installer avec les options par défaut

**Vérification:**
```powershell
git --version
# git version 2.43.x
```

### 🐧 Linux
```bash
sudo apt install git -y

# Vérification
git --version
# git version 2.x.x
```

### Configuration initiale
```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"
```

✅ **Git installé avec succès !**

## 🚀 Étape 3 : Création du Projet

### 3.1 Créer le dossier du projet

**🪟 Windows (PowerShell):**
```powershell
mkdir playwright-pytest-hatch-tutorial
cd playwright-pytest-hatch-tutorial
git init
```

**🐧 Linux:**
```bash
mkdir playwright-pytest-hatch-tutorial
cd playwright-pytest-hatch-tutorial
git init
```

---

### 3.2 Créer la structure complète

**🪟 Windows:**
```powershell
# Dossiers source
New-Item -ItemType Directory -Path "src\tutorial_tests\pages" -Force

# Dossiers tests
New-Item -ItemType Directory -Path "tests\unit" -Force
New-Item -ItemType Directory -Path "tests\integration" -Force
New-Item -ItemType Directory -Path "tests\e2e" -Force

# Dossiers résultats
New-Item -ItemType Directory -Path "test-results\screenshots" -Force
New-Item -ItemType Directory -Path "test-results\videos" -Force
New-Item -ItemType Directory -Path "test-results\traces" -Force

# Dossier authentification
New-Item -ItemType Directory -Path "playwright\.auth" -Force

# Fichiers Python
New-Item -ItemType File -Path "src\tutorial_tests\__init__.py" -Force
New-Item -ItemType File -Path "src\tutorial_tests\pages\__init__.py" -Force
```

**🐧 Linux:**
```bash
# Dossiers
mkdir -p src/tutorial_tests/pages
mkdir -p tests/{unit,integration,e2e}
mkdir -p test-results/{screenshots,videos,traces}
mkdir -p playwright/.auth

# Fichiers Python
touch src/tutorial_tests/__init__.py
touch src/tutorial_tests/pages/__init__.py
```

---

### 3.3 Structure obtenue
```
playwright-pytest-hatch-tutorial/
├── 📁 src/
│   └── 📁 tutorial_tests/
│       ├── 📄 __init__.py
│       └── 📁 pages/
│           └── 📄 __init__.py
│
├── 📁 tests/
│   ├── 📄 conftest.py           (étape 4)
│   ├── 📁 unit/
│   ├── 📁 integration/
│   └── 📁 e2e/
│       ├── 📄 conftest.py       (étape 4)
│       └── 📄 test_login.py     (étape 6)
│
├── 📁 test-results/
│   ├── 📁 screenshots/
│   ├── 📁 videos/
│   └── 📁 traces/
│
├── 📁 playwright/.auth/
├── 📄 pyproject.toml            (étape 4)
└── 📄 .gitignore                (étape 4)
```

✅ **Structure créée avec succès !**

---

## 🔧 Étape 4 : Configuration

### 4.1 Créer .gitignore

**Créer le fichier:**
```bash
# Windows
New-Item -ItemType File -Path ".gitignore" -Force

# Linux
touch .gitignore
```
---

### 4.2 Créer pyproject.toml

**Créer le fichier:**
```bash
# Windows
New-Item -ItemType File -Path "pyproject.toml" -Force

# Linux
touch pyproject.toml
```

---

### 4.3 Installer les dépendances
```bash
# Créer l'environnement
hatch env create

# Installer les navigateurs Playwright
hatch run install-browsers
```

**⏱️ Durée:** 3-5 minutes

**📦 Installation:**
- ✅ pytest + plugins
- ✅ playwright
- ✅ rich (logs colorés)
- ✅ allure-pytest
- ✅ Navigateurs (Chromium, Firefox, WebKit)

---

### 4.4 Créer tests/conftest.py (global)

**Créer le fichier:**
```bash
# Windows
New-Item -ItemType File -Path "tests\conftest.py" -Force

# Linux
touch tests/conftest.py

---

### 4.5 Créer tests/e2e/conftest.py

**Créer le fichier:**
```bash
# Windows
New-Item -ItemType File -Path "tests\e2e\conftest.py" -Force

# Linux
touch tests/e2e/conftest.py
```

---

✅ **Configuration terminée !**

---

## 🎨 Étape 5 : Création des Page Objects

### 5.1 Créer src/tutorial_tests/pages/login_page.py

**Créer le fichier:**
```bash
# Windows
New-Item -ItemType File -Path "src\tutorial_tests\pages\login_page.py" -Force

# Linux
touch src/tutorial_tests/pages/login_page.py
```

✅ **LoginPage créé !**


## ✅ Étape 6 : Premier Test

### 6.1 Créer tests/e2e/test_login.py

**Créer le fichier:**
```bash
# Windows
New-Item -ItemType File -Path "tests\e2e\test_login.py" -Force

# Linux
touch tests/e2e/test_login.py

---

### 6.2 Lancer les tests
```bash
# Tous les tests
hatch run test

# Tests smoke uniquement
hatch run test-smoke

# Mode visible (headed)
hatch run test-headed
```

**✅ Les tests devraient passer !**

---

## 🚀 Étape 7 : CI/CD GitHub Actions

### 7.1 Créer le dossier
```bash
# Windows
New-Item -ItemType Directory -Path ".github\workflows" -Force

# Linux
mkdir -p .github/workflows
```

---

### 7.2 Créer .github/workflows/playwright-tests.yml
```yaml

---

### 7.3 Pousser sur GitHub
```bash
git add .
git commit -m "feat: Initial setup with Playwright, Pytest and Hatch"
git remote add origin https://github.com/VOTRE-USERNAME/playwright-pytest-hatch-tutorial.git
git branch -M main
git push -u origin main
```

**✅ GitHub Actions se lance automatiquement !**

---

## 🎨 Étape 8 : Installation Allure (Optionnel)

### 8.1 Installer Scoop (Windows)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

### 8.2 Installer Java et Allure
```powershell
scoop bucket add java
scoop install openjdk
scoop install allure
```

### 8.3 Utiliser Allure
```bash
# Lancer les tests avec Allure
hatch run test-allure

# Voir le rapport
hatch run allure-serve
```

**🎉 Le rapport s'ouvre dans le navigateur !**

---

## 🛠️ Troubleshooting

### ❌ "Cannot remove active environment"

**Solution:**
```bash
exit  # Sortir du shell Hatch
hatch env remove default
```

---

### ❌ "Browser not found"

**Solution:**
```bash
hatch run install-browsers
```

---

### ❌ "java command not found"

**Solution:**
```bash
scoop install openjdk
```

---

### ❌ Tests échouent en CI

**Cause:** Mode headless mal configuré

**Vérifier:** `is_ci = os.getenv("CI")` dans `conftest.py`

---
