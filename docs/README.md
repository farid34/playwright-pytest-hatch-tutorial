# 🎭 Playwright + Pytest avec Hatch - Guide Complet

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

- [À propos](#à-propos)
- [Démarrage Rapide](#démarrage-rapide)
- [Documentation](#documentation)
- [Structure du Projet](#structure-du-projet)
- [Utilisation](#utilisation)
- [CI/CD](#cicd)
- [Contribution](#contribution)

---

## 🎯 À propos

Ce projet documente l'apprentissage et la mise en place d'un framework de tests automatisés web utilisant :
- **Playwright** - Automatisation de navigateur moderne et rapide
- **Pytest** - Framework de tests Python flexible
- **Hatch** - Gestionnaire de projet Python moderne
- **GitHub Actions** - Pipeline CI/CD

### 🎓 Objectifs d'apprentissage

- [x] Comprendre Hatch et la gestion moderne de projets Python
- [x] Maîtriser Playwright pour l'automatisation web
- [ ] Implémenter le pattern Page Object Model (POM)
- [ ] Configurer une pipeline CI/CD complète
- [ ] Écrire des tests robustes et maintenables

---

## 🚀 Démarrage Rapide

### Prérequis

- Python 3.12+
- Git
- Compte GitHub

### Installation Express
```bash
# 1. Cloner le repository
git clone https://github.com/VOTRE-USERNAME/playwright-pytest-hatch-tutorial.git
cd playwright-pytest-hatch-tutorial

# 2. Installer Hatch
pip install hatch

# 3. Créer l'environnement et installer les dépendances
hatch env create

# 4. Installer les navigateurs Playwright
hatch run install-browsers

# 5. Lancer les tests
hatch run test
```

**Pour une installation détaillée :** Consultez [INSTALLATION.md](INSTALLATION.md)

---

## 📚 Documentation

### 📖 Guides Principaux

| Guide | Description | Compatibilité |
|-------|-------------|---------------|
| [📥 INSTALLATION.md](INSTALLATION.md) | Guide d'installation rapide | Windows / Linux |
| [🎯 HATCH_GUIDE.md](HATCH_GUIDE.md) | Référence rapide Hatch | Windows / Linux |
| [📝 LESSONS_LEARNED.md](LESSONS_LEARNED.md) | Notes d'apprentissage | - |

### 📂 Documentation Détaillée

Toute la documentation pas-à-pas est dans le dossier **`docs/`** :

**➡️ [Accéder à la documentation complète](docs/README.md)**

| Étape | Guide | Windows | Linux |
|-------|-------|---------|-------|
| 0 | [Configuration Git/GitHub](docs/00-github-setup.md) | ✅ | ✅ |
| 1 | [Installation Python](docs/01-setup-environment.md) | ✅ | ✅ |
| 2 | [Installation Hatch](docs/02-hatch-installation.md) | ✅ | ✅ |
| 3 | [Création du projet](docs/03-project-creation.md) | ✅ | ✅ |

**Chaque guide contient :**
- Instructions pas-à-pas
- Explications détaillées
- Résolution de problèmes
- Sections spécifiques Windows **ET** Linux

---

## 📁 Structure du Projet
```
playwright-pytest-hatch-tutorial/
├── 📄 README.md                    # Ce fichier
├── 📄 INSTALLATION.md              # Guide installation rapide
├── 📄 HATCH_GUIDE.md               # Référence Hatch
├── 📄 LESSONS_LEARNED.md           # Notes personnelles
├── 📄 pyproject.toml               # Configuration Hatch
├── 📄 .gitignore
│
├── 📁 docs/                        # Documentation détaillée
│   ├── 📄 README.md                # Index de navigation
│   ├── 📄 00-github-setup.md
│   ├── 📄 01-setup-environment.md
│   ├── 📄 02-hatch-installation.md
│   └── 📄 03-project-creation.md
│
├── 📁 src/                         # Code source (à venir)
│   └── 📁 ecommerce_tests/
│       └── 📁 pages/               # Page Object Models
│
├── 📁 tests/                       # Tests (à venir)
│   ├── 📄 conftest.py
│   └── 📄 test_*.py
│
└── 📁 .github/                     # CI/CD (à venir)
    └── 📁 workflows/
        └── 📄 tests.yml
```

---

## 🎮 Utilisation

### Commandes Essentielles
```bash
# Lancer tous les tests
hatch run test

# Tests en mode visible (headed)
hatch run test-headed

# Tests avec rapport HTML
hatch run test-report

# Tests smoke uniquement
hatch run test-smoke

# Tests parallèles
hatch run test-parallel
```

### Ajouter un nouveau test

1. Créer `test_*.py` dans `tests/`
2. Importer les pages depuis `src/ecommerce_tests/pages/`
3. Écrire les tests avec Pytest
4. Lancer : `hatch run test`

---

## 🔄 CI/CD

Le projet utilise **GitHub Actions** pour l'intégration continue.

**Workflow :** `.github/workflows/tests.yml`

**Déclencheurs :**
- Push sur `main` ou `develop`
- Pull Request vers `main`

**Pipeline :**
1. Installation Python 3.12
2. Installation Hatch
3. Installation navigateurs Playwright
4. Exécution des tests
5. Upload des rapports (si échec)

---

## 📚 Ressources

### Documentation Officielle
- [Playwright Python](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/)
- [Hatch](https://hatch.pypa.io/)
- [Python](https://docs.python.org/3/)

### Cours Suivis
- [Coursera - Playwright Python and Pytest](https://www.coursera.org/learn/packt-playwright-python-and-pytest-for-web-automation-testing)

---

## 🤝 Contribution

Ce projet est à but pédagogique. Contributions bienvenues !

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit (`git commit -m '✨ Add: nouvelle fonctionnalité'`)
4. Push (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

---

## 📜 Licence

MIT License - Libre d'utilisation pour l'apprentissage

---

## ✍️ Auteur

**Abdelhamid Farid**
- GitHub: [@farid34](https://github.com/farid34)
- Formation: Coursera Playwright Python & Pytest
- Date: Novembre 2025

---

## 🌟 Remerciements

- [Coursera](https://www.coursera.org/) pour la formation
- La communauté Playwright et Pytest

---

## 📝 Notes

**Statut du projet :** 🚧 En cours de développement

**Dernière mise à jour :** 26/11/2025

**Prochaines étapes :**
- [ ] Créer le projet Hatch
- [ ] Implémenter les Page Object Models
- [ ] Écrire les tests
- [ ] Configurer la CI/CD
```

**Sauvegardez.**

---

## 📊 Visualisation de la structure
```
Visiteur GitHub arrive sur votre repo
            │
            ▼
    📄 README.md (racine)
    "Page d'accueil du projet"
            │
            ├─→ Démarrage rapide
            ├─→ Liens vers INSTALLATION.md
            ├─→ Lien vers HATCH_GUIDE.md
            └─→ Lien vers docs/ pour détails
                        │
                        ▼
                📁 docs/README.md
                "Index de navigation"
                        │
                        ├─→ 00-github-setup.md
                        ├─→ 01-setup-environment.md
                        ├─→ 02-hatch-installation.md
                        └─→ 03-project-creation.md