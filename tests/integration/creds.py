import os

GH_ACCESS_TOKEN = os.getenv("GH_ACCESS_TOKEN")

if not GH_ACCESS_TOKEN:
    raise ValueError("GITHUB_ACCESS_TOKEN non défini. Ajoute-le dans .env ou en variable d'environnement.")

GITHUB_USER = "farid34"

GITHUB_REPO = "test_repo"