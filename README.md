<h1 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=38BDF8&center=true&vCenter=true&width=700&height=60&lines=Cloud+Infrastructure+%26+CI%2FCD+Pipeline;Zero-Downtime+Containerized+Deployment;Automated+Edge+Security+%26+Nginx+Proxy" alt="Typing SVG" />
</h1>

<p align="center">
  <img src="https://github.com/Moizzaman/cloud-cicd-pipeline/actions/workflows/deploy.yml/badge.svg" alt="CI/CD Status" />
  <img src="https://img.shields.io/badge/CONTAINER-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white&color=1e293b&labelColor=2496ED" alt="Docker" />
  <img src="https://img.shields.io/badge/PROXY-Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white&color=1e293b&labelColor=009639" alt="Nginx" />
  <img src="https://img.shields.io/badge/BACKEND-Python%20Flask-3776AB?style=for-the-badge&logo=python&logoColor=white&color=1e293b&labelColor=3776AB" alt="Python" />
</p>

---

<p align="center">
  <code>$ cat ~/pipeline-overview.md</code><br>
  <em>An enterprise-grade, automated infrastructure stack designed to route client traffic securely through an edge reverse proxy into a multi-worker application container cluster with automated GitHub Actions testing.</em>
</p>

---

## 📐 System Architecture Flow

```text
 ┌─────────────────┐           HTTP (Port 80)          ┌─────────────────────────┐
 │   Client Traffic│ ────────────────────────────────► │   Nginx Reverse Proxy   │
 └─────────────────┘                                   │ - Rate Limiting (10r/s) │
                                                       │ - Security Header Guard │
                                                       └────────────┬────────────┘
                                                                    │
                                                          Proxy Pass (Port 5000)
                                                                    │
                                                                    ▼
                                                       ┌─────────────────────────┐
                                                       │  Dockerized Gunicorn    │
                                                       │  Python App (3 Workers) │
                                                       └─────────────────────────┘
