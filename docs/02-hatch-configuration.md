# 🎯 Étape 2 : Installation de Hatch

## Date : 26/11/2025

---

## 🎯 Objectif

Installer Hatch, le gestionnaire de projet Python moderne qui remplacera venv + pip.

---

## 📋 Prérequis

Avant cette étape, vous devez avoir :
- [x] Python 3.12 installé ([Étape 1](01-setup-environment.md))
- [x] pip fonctionnel
- [x] PATH configuré correctement

---

## 🤔 C'est quoi Hatch ?

### Définition

**Hatch** = Gestionnaire de projet Python tout-en-un

### Que fait Hatch ?
```
Hatch remplace :
├─ venv (environnements virtuels)
├─ pip (gestion des dépendances)
├─ requirements.txt (fichier de dépendances)
├─ setup.py (configuration du projet)
└─ Makefile/scripts bash (automatisation)

Tout centralisé dans : pyproject.toml
```

---

## 🆚 Hatch vs Approche Traditionnelle

### Sans Hatch (méthode classique)
```powershell
# 1. Créer environnement virtuel
python -m venv venv

# 2. Activer l'environnement
venv\Scripts\activate

# 3. Installer dépendances
pip install -r requirements.txt

# 4. Lancer tests
pytest

# 5. Désactiver
deactivate
```

**Problèmes :**
- ❌ Beaucoup de commandes à retenir
- ❌ Activation/désactivation manuelle
- ❌ Plusieurs fichiers de configuration
- ❌ Difficile de gérer plusieurs environnements

---

### Avec Hatch (méthode moderne)
```powershell
# 1. Créer environnement + installer dépendances
hatch env create

# 2. Lancer tests
hatch run test

# C'est tout ! ✨
```

**Avantages :**
- ✅ Commandes simples
- ✅ Pas d'activation manuelle
- ✅ Un seul fichier : pyproject.toml
- ✅ Environnements multiples faciles
- ✅ Scripts personnalisés

---

## 📊 Comparaison détaillée

| Action | venv + pip | Hatch |
|--------|------------|-------|
| **Créer env** | `python -m venv venv` | Automatique |
| **Activer** | `venv\Scripts\activate` | Pas besoin |
| **Installer deps** | `pip install -r requirements.txt` | `hatch env create` |
| **Lancer tests** | `pytest` | `hatch run test` |
| **Ajouter dep** | Éditer requirements.txt + `pip install` | Éditer pyproject.toml |
| **Multi-env** | Gérer plusieurs venv manuellement | Facile via pyproject.toml |
| **Scripts** | Créer scripts bash/Makefile | Intégré dans pyproject.toml |

---

## 💻 Installation de Hatch

### Commande
```powershell
pip install hatch
```

### Ce qui se passe
```
Collecting hatch
  Downloading hatch-1.9.4-py3-none-any.whl (...)
Collecting click>=8.0.6
  Downloading click-8.1.7-py3-none-any.whl
Collecting hyperlink>=21.0.0
  Downloading hyperlink-21.0.0-py2.py3-none-any.whl
...
Installing collected packages: ...
Successfully installed hatch-1.9.4 click-8.1.7 hyperlink-21.0.0 ...
```

**Temps d'installation :** 30-60 secondes

---

### Résultat
```
✅ Hatch installé globalement
✅ Commande 'hatch' disponible
✅ Installé dans : C:\Users\Admin\AppData\Local\Programs\Python\Python312\Scripts\
```

---

## ✅ Vérification de l'installation

### Test 1 : Version
```powershell
hatch --version
```

**Résultat attendu :**
```
Hatch, version 1.9.4
```

---

### Test 2 : Aide
```powershell
hatch --help
```

**Résultat attendu :**
```
Usage: hatch [OPTIONS] COMMAND [ARGS]...

  Hatch is a modern, extensible Python project manager.

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  build      Build a project.
  clean      Remove build artifacts.
  config     Manage the config file.
  env        Manage project environments.
  new        Create a new project.
  run        Run commands within project environments.
  ...
```

---

### Test 3 : Localisation
```powershell
where.exe hatch
```

**Résultat attendu :**
```
C:\Users\Admin\AppData\Local\Programs\Python\Python312\Scripts\hatch.exe
```

✅ **Hatch est bien dans le dossier Scripts !**

---

## 🎓 Commandes Hatch de base

### Gestion de projet
```powershell
# Créer un nouveau projet
hatch new mon-projet

# Initialiser Hatch dans un projet existant
hatch new --init
```

---

### Gestion des environnements
```powershell
# Créer/mettre à jour l'environnement
hatch env create

# Lister les environnements
hatch env show

# Supprimer un environnement
hatch env remove default

# Supprimer tous les environnements
hatch env prune
```

---

### Exécution de commandes
```powershell
# Exécuter une commande dans l'environnement par défaut
hatch run python --version
hatch run pip list

# Exécuter un script personnalisé
hatch run test
hatch run lint

# Exécuter dans un environnement spécifique
hatch run test:pytest
```

---

## 📄 Structure d'un projet Hatch

### Fichier central : pyproject.toml
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mon-projet"
version = "0.1.0"
dependencies = [
    "playwright>=1.40.0",
    "pytest>=7.4.0",
]

[tool.hatch.envs.default]
dependencies = [
    "pytest-playwright",
]

[tool.hatch.envs.default.scripts]
test = "pytest {args}"
lint = "ruff check ."
```

**Tout est dans UN SEUL fichier ! ✨**

---

## 🔧 Concepts clés Hatch

### 1. Environnements
```
Hatch peut gérer plusieurs environnements :

default → Développement quotidien
test → Tests uniquement
docs → Génération de documentation
lint → Vérification du code
```

**Configuration :**
```toml
[tool.hatch.envs.default]
dependencies = ["pytest"]

[tool.hatch.envs.lint]
dependencies = ["ruff", "mypy"]
```

**Utilisation :**
```powershell
hatch run test           # Env default
hatch run lint:check     # Env lint
```

---

### 2. Scripts personnalisés
```toml
[tool.hatch.envs.default.scripts]
test = "pytest {args}"
test-cov = "pytest --cov {args}"
```

**Utilisation :**
```powershell
hatch run test                    # pytest
hatch run test tests/test_login.py  # pytest tests/test_login.py
hatch run test-cov                # pytest --cov
```

**`{args}` = Arguments passés au script**

---

### 3. Pas d'activation manuelle
```
❌ Avec venv :
venv\Scripts\activate
pytest
deactivate

✅ Avec Hatch :
hatch run test
(Hatch gère l'activation automatiquement !)
```

---

## 🐛 Problèmes potentiels et solutions

### Problème 1 : "hatch: command not found"

**Cause :** Hatch n'est pas dans le PATH

**Solution 1 :** Utiliser via Python
```powershell
python -m hatch --version
py -m hatch --version
```

**Solution 2 :** Ajouter Scripts au PATH
```
C:\Users\Admin\AppData\Local\Programs\Python\Python312\Scripts
```

---

### Problème 2 : Conflits avec pip

**Symptôme :** `pip install hatch` ne fonctionne pas

**Solution :**
```powershell
# Mettre à jour pip
python -m pip install --upgrade pip

# Réinstaller Hatch
python -m pip install hatch
```

---

### Problème 3 : Environnement corrompu

**Solution :**
```powershell
# Supprimer et recréer
hatch env remove default
hatch env create
```

---

## 🎯 Hatch vs autres outils

### Hatch vs Poetry

| Aspect | Hatch | Poetry |
|--------|-------|--------|
| **Philosophie** | Simple et flexible | Complet mais strict |
| **Configuration** | pyproject.toml | pyproject.toml + poetry.lock |
| **Environnements** | ✅ Faciles | ⚠️ Un seul par défaut |
| **Vitesse** | ⭐⭐⭐⭐ Rapide | ⭐⭐⭐ Moyen |
| **Courbe apprentissage** | ⭐⭐⭐ Facile | ⭐⭐⭐⭐ Plus complexe |

---

### Hatch vs Pipenv

| Aspect | Hatch | Pipenv |
|--------|-------|--------|
| **Fichier lock** | Non | Oui (Pipfile.lock) |
| **Scripts** | ✅ Intégrés | ⚠️ Basiques |
| **Multi-env** | ✅ Natif | ❌ Difficile |
| **Maintenance** | ✅ Actif | ⚠️ Moins actif |

---

## 📚 Ressources

### Documentation officielle
- [Hatch](https://hatch.pypa.io/)
- [Tutoriel Hatch](https://hatch.pypa.io/latest/tutorials/python/getting-started/)
- [Configuration Reference](https://hatch.pypa.io/latest/config/project/)

### Exemples
- [Hatch sur GitHub](https://github.com/pypa/hatch)
- [Exemples de projets](https://hatch.pypa.io/latest/community/users/)

---

## ✅ Résultat final

- [x] Hatch 1.9.4 installé
- [x] Commande `hatch` fonctionnelle
- [x] hatch.exe dans Scripts
- [x] Commandes de base comprises
- [x] Prêt à créer des projets

---

## 💡 Pourquoi Hatch pour notre projet ?

### Avantages pour Playwright + Pytest

1. **Environnements isolés** → Pas de conflits de dépendances
2. **Scripts personnalisés** → `hatch run test-headed`, `hatch run test-smoke`
3. **Configuration centralisée** → Tout dans pyproject.toml
4. **CI/CD simple** → Même commandes en local et sur GitHub Actions
5. **Multi-environnements** → dev, test, docs facilement

---

## 🔜 Prochaine étape

[Création du projet avec Hatch](03-project-creation.md)

---

## 📝 Notes personnelles

### Comparaison avec venv

**Avant (venv) :**
- Création manuelle du venv
- Activation à chaque session
- requirements.txt séparé
- Scripts bash pour automatisation

**Maintenant (Hatch) :**
- Tout automatique
- Pas d'activation
- Configuration dans pyproject.toml
- Scripts intégrés

**Gain de temps estimé : 30% ⏱️**

---

## 🎓 Concepts à retenir

### 1. pyproject.toml = Centre de contrôle

Un seul fichier pour :
- Métadonnées du projet
- Dépendances
- Environnements
- Scripts
- Configuration des outils (pytest, coverage, etc.)

---

### 2. Environnements automatiques
```
Hatch crée les environnements dans :
.hatch/env/virtual/

Vous n'avez JAMAIS à les manipuler directement !
```

---

### 3. Scripts = Raccourcis
```toml
test = "pytest {args}"

= Au lieu de taper :
  pytest --headed --slowmo=500 tests/test_login.py

  Vous tapez :
  hatch run test --headed --slowmo=500 tests/test_login.py
```

---

## ✨ Citation

> "Hatch is designed to be a unified interface for managing Python projects from creation to publishing."
> — Hatch Documentation

---

## 🎯 Checklist avant de passer à l'étape 3

- [ ] `hatch --version` fonctionne
- [ ] Compris la différence venv vs Hatch
- [ ] Compris le rôle de pyproject.toml
- [ ] Compris les environnements Hatch
- [ ] Compris les scripts personnalisés
- [ ] Prêt à initialiser le projet