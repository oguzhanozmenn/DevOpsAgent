import httpx


class GitHubService:
    async def get_repo_files(self, repo_url: str):
        # Örnek link: https://github.com/user/repo
        # API linki: https://api.github.com/repos/user/repo/contents
        parts = repo_url.rstrip("/").split("/")
        user, repo = parts[-2], parts[-1]
        api_url = f"https://api.github.com/repos/{user}/{repo}/contents"

        async with httpx.AsyncClient() as client:
            response = await client.get(api_url)
            if response.status_code == 200:
                contents = response.json()
                # Sadece dosya isimlerini çekelim
                return [item["name"] for item in contents]
            return []

    def analyze_files(self, file_list: list):
        analysis = {"project_type": "Unknown", "suggested_docker_image": "python:3.9-slim"}

        if "package.json" in file_list:
            analysis.update({"project_type": "Node.js", "suggested_docker_image": "node:18-alpine"})
        elif "requirements.txt" in file_list or "main.py" in file_list:
            analysis.update({"project_type": "Python", "suggested_docker_image": "python:3.11-slim"})

        return analysis