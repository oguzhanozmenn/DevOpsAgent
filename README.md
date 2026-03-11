# 🤖 AI DevOps Agent

AI-powered assistant that analyzes repositories and generates production-ready DevOps artifacts.

## 🚀 Proje Amacı
Geliştiricilerin sadece bir komutla ("Bu projeyi AWS'e deploy et") tüm altyapıyı hazır bulmasını sağlamak. Sistem otomatik olarak:
- 🔍 Repo analizi yapar.
- 🐳 Dockerfile üretir.
- 🏗️ Terraform (IaC) dosyalarını hazırlar.
- 🛡️ CI/CD pipeline'larını kurar.

## 🏗️ Sistem Mimarisi
- **Backend:** FastAPI (Python)
- **Orchestrator:** AI Agent System (Multi-Agent Architecture)
- **Deployment:** AWS / Kubernetes

## 🛠️ Kurulum (Geliştiriciler İçin)
1. Projeyi klonlayın.
2. `pip install -r requirements.txt` ile bağımlılıkları yükleyin.
3. `.env` dosyasını oluşturun ve API anahtarlarınızı ekleyin.