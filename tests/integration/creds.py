import os

# Le workflow GitHub Actions fournit une variable d'env nommée GITHUB_ACCESS_TOKEN
GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")

if not GITHUB_ACCESS_TOKEN:
    raise ValueError(
        "GITHUB_ACCESS_TOKEN non défini. " \
        "Ajoute-le dans .env ou en variable d'environnement."
    )

GITHUB_USER = "farid34"

GITHUB_REPO = "test_repo"