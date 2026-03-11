from fastapi import FastAPI
from pydantic import BaseModel

# Ajanlarımızı ve servislerimizi içeri aktarıyoruz
from app.services.github_service import GitHubService
from app.agents.docker.docker_agent import DockerAgent
from app.agents.cicd.cicd_agent import CICDAgent

# 1. Uygulama ve Araçların Başlatılması
app = FastAPI(
    title="AI DevOps Agent API",
    description="Analiz, Docker ve CI/CD süreçlerini otomatize eden yapay zeka destekli asistan.",
    version="0.1.0"
)

github_tool = GitHubService()
docker_agent = DockerAgent()
cicd_agent = CICDAgent()


# 2. Veri Modeli (Kullanıcının göndereceği veri yapısı)
class RepoRequest(BaseModel):
    repo_url: str


# 3. Ana Sayfa Endpoint'i
@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "AI DevOps Agent is ready and armed with Docker & CI/CD tools!",
        "version": "0.1.0"
    }


# 4. Repo Analiz Endpoint'i (Sadece analiz yapar)
@app.post("/analyze")
async def analyze_repo(request: RepoRequest):
    # Canlı GitHub verisini çek
    real_files = await github_tool.get_repo_files(request.repo_url)

    if not real_files:
        return {"status": "error", "message": "Repo not found or empty. Check the URL!"}

    # Dosyaları analiz et (Dil ve araç tespiti)
    result = github_tool.analyze_files(real_files)

    return {
        "status": "success",
        "repo": request.repo_url,
        "files_found": real_files,
        "analysis_result": result
    }


# 5. Dockerfile Üretme Endpoint'i
@app.post("/generate-docker")
async def generate_docker(request: RepoRequest):
    # Analiz sonucuna göre Dockerfile üret
    files = await github_tool.get_repo_files(request.repo_url)
    analysis = github_tool.analyze_files(files)

    dockerfile_content = docker_agent.generate_dockerfile(analysis)

    return {
        "status": "success",
        "project_type": analysis["project_type"],
        "dockerfile": dockerfile_content
    }


# 6. CI/CD (GitHub Actions) Üretme Endpoint'i
@app.post("/generate-cicd")
async def generate_cicd(request: RepoRequest):
    # Analiz sonucuna göre YAML dosyası üret
    files = await github_tool.get_repo_files(request.repo_url)
    analysis = github_tool.analyze_files(files)

    actions_content = cicd_agent.generate_github_actions(analysis)

    return {
        "status": "success",
        "project_type": analysis["project_type"],
        "github_actions_yaml": actions_content
    }