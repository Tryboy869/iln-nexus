
# scripts/update_stats.py
import os
import re
from datetime import datetime
import requests

# Les variables sont définies à l'intérieur de ce script,
# car il sera exécuté indépendamment par GitHub Actions.
REPO_NAME = "Tryboy869/iln-nexus"
README_PATH = "README.md"

def get_repo_stats(repo_name):
    """Récupère les stats via l'API GitHub."""
    try:
        token = os.getenv('GITHUB_TOKEN')
        headers = {'Authorization': f'token {token}'} if token else {}
        response = requests.get(f"https://api.github.com/repos/{repo_name}", headers=headers)
        response.raise_for_status()
        data = response.json()
        return {
            "stars": data.get("stargazers_count", 0),
            "last_commit_date": data.get("pushed_at", "N/A"),
        }
    except Exception as e:
        print(f"Could not fetch real GitHub stats: {e}")
        return {"stars": "N/A", "last_commit_date": "N/A"}

def update_readme(stats):
    """Injecte les statistiques dans le README.md."""
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    last_commit_str = "N/A"
    if stats['last_commit_date'] != 'N/A':
        try:
            date_obj = datetime.fromisoformat(stats['last_commit_date'].replace('Z', '+00:00'))
            last_commit_str = date_obj.strftime('%d %B %Y')
        except ValueError:
            last_commit_str = stats['last_commit_date']

    # Notez l'utilisation de f-strings ici, qui seront évaluées lorsque ce script s'exécutera.
    stats_block = f"""
*Dernière mise à jour : {datetime.utcnow().strftime('%d %B %Y, %H:%M:%S UTC')}*
* **Révolutionnaires (Stars) :** [![GitHub Stars](https://img.shields.io/github/stars/{REPO_NAME}?style=social)](https://github.com/{REPO_NAME}/stargazers)
* **Dernier Commit :** [![Last Commit](https://img.shields.io/github/last-commit/{REPO_NAME}?style=flat-square&color=blueviolet&label={last_commit_str})](https://github.com/{REPO_NAME}/commits/main)
* **Build Status :** [![Build Status](https://img.shields.io/github/actions/workflow/status/{REPO_NAME}/update_readme.yml?style=flat-square&label=README%20Status)](https://github.com/{REPO_NAME}/actions)
"""

    new_content = re.sub(
        r"(?s)<!-- START_STATS -->.*?<!-- END_STATS -->",
        f"<!-- START_STATS -->\n{stats_block}\n<!-- END_STATS -->",
        content,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("✅ README.md a été mis à jour avec les nouvelles statistiques.")

if __name__ == "__main__":
    print("🚀 Lancement du script de mise à jour du README...")
    repo_stats = get_repo_stats(REPO_NAME)
    update_readme(repo_stats)
    print("✨ Processus terminé.")
