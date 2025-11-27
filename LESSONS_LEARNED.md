## 📅 27/11/2025

### ⚠️ Erreur : Documentation vs Réalité

**Problème rencontré :**
- Documenté l'installation de Hatch dans les guides
- **Mais oublié de vraiment l'installer !**

**Leçon critique :**
> Documenter n'est PAS installer. Il faut **exécuter ET documenter** en parallèle.

**Bonne pratique identifiée :**
Workflow correct :
1. ✅ Exécuter la commande
2. ✅ Vérifier que ça marche
3. ✅ Documenter ce qu'on a fait
4. ❌ NE PAS documenter avant d'avoir testé

**Solution appliquée :**
```powershell
pip install hatch
hatch --version  # Vérification
```

**Checklist de vérification ajoutée :**
- [ ] Python installé ET vérifié
- [ ] pip installé ET vérifié
- [ ] Hatch installé ET vérifié
- [ ] Commandes testées dans le terminal

---

### 🔧 Hatch vs Hatchling

**Question :**
Faut-il installer `hatch` ou `hatchling` ?

**Réponse :**
- ✅ **Installer : `hatch`** (l'outil CLI)
- ❌ **Ne PAS installer : `hatchling`** (dépendance automatique)

**Comprendre la différence :**
- `hatch` = Gestionnaire de projet (ce qu'on utilise)
- `hatchling` = Build backend (utilisé en interne)

**Commande unique :**
```powershell
pip install hatch
```

**Vérification :**
```powershell
hatch --version        # Hatch
pip show hatchling     # Installé automatiquement
```

**Dans pyproject.toml :**
```toml
[build-system]
requires = ["hatchling"]  # Déclare la dépendance
build-backend = "hatchling.build"
```
Ceci indique à Python quel système de build utiliser, mais hatchling est déjà installé avec hatch.

---
Sauvegardez.

🎯 Confirmation
Vous avez installé :
powershellpip install hatch
Vérifiez que les deux sont présents :
powershellhatch --version
pip show hatchling
Si les deux commandes fonctionnent, vous êtes prêt ! ✅

🚀 On peut continuer ?
Confirmez-moi que :

✅ hatch --version affiche la version
✅ pip show hatchling affiche des infos

Et on reprend la création du projet ! 🎭RéessayerClaude peut faire des erreurs. Assurez-vous de vérifier ses réponses.