# ☁️ Automated Cloud CI/CD & Reverse Proxy Pipeline

[![CI/CD Pipeline](https://github.com/Moizzaman/cloud-cicd-pipeline/actions/workflows/deploy.yml/badge.svg)](https://github.com/Moizzaman/cloud-cicd-pipeline/actions)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/Reverse%20Proxy-Nginx-009639?style=flat-square&logo=nginx)](https://nginx.org/)
[![Python](https://img.shields.io/badge/Backend-Python%20Flask-3776AB?style=flat-square&logo=python)](https://flask.palletsprojects.com/)

An automated, containerized infrastructure pipeline featuring zero-downtime deployment workflows, Nginx reverse proxying with security hardening, and GitHub Actions CI/CD automation.

---

## 📐 System Architecture

```text
 ┌─────────────────┐           HTTP (Port 80)          ┌─────────────────────────┐
 │   Client Traffic│ ────────────────────────────────► │   Nginx Reverse Proxy   │
 └─────────────────┘                                   │ - Rate Limiting (10r/s) │
                                                       │ - Security Headers      │
                                                       └────────────┬────────────┘
                                                                    │
                                                          Proxy Pass (Port 5000)
                                                                    │
                                                                    ▼
                                                       ┌─────────────────────────┐
                                                       │  Dockerized Gunicorn    │
                                                       │  Python App (3 Workers) │
                                                       └─────────────────────────┘