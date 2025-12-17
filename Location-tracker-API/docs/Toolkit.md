# Location Tracker API Developer Toolkit

This toolkit provides essential resources, guidelines, and utilities for working with the **Location Tracker API Multi‑Stack Project**. Use this as a quick reference while developing, testing, or extending any of the FastAPI, Flask, Express, or Rust implementations.

---

## 📦 Project Overview

The Location Tracker API project provides unified endpoints for tracking and retrieving location information using multiple backend technologies. Each stack follows the same routing logic for consistency:

* `POST /locations` — Add a new location
* `GET /locations` — Retrieve latest locations for all users
* `GET /locations/{user_id}` — Get latest location for a specific user
* `GET /locations/{user_id}/history` — Get location history for a user

---

## ⚙️ Development Tools

* **VS Code Extensions**

  * Python
  * Rust Analyzer
  * Prettier
  * ESLint
  * Docker

* **CLI Tools**

  * `curl` for manual endpoint testing
  * `docker compose` for multi‑service orchestration
  * `httpie` (optional) for clean HTTP requests

---

## 🧪 Testing Toolkit

### Quick Commands

```bash
# FastAPI
pytest

# Node.js
npm test

# Flask
pytest

# Rust (Actix)
cargo test
```

### Testing Guidelines

* Write unit tests for handlers and helpers
* Add integration tests that hit actual running services
* Use mocks for external API calls when possible

---

## 🚀 Deployment Toolkit

### Docker

Each service includes:

* `Dockerfile`
* `.dockerignore`

Start all services:

```bash
docker compose up --build
```

### CI/CD (GitHub Actions)

Features:

* Linting
* Tests
* Docker build
* Security checks (npm audit, pip audit, cargo audit)

---

## 🔐 Security Toolkit

Recommended additions:

* API key or JWT-based authentication
* Rate limiting middleware
* CORS restrictions
* Logging + monitoring with OpenTelemetry
* Input validation to avoid injection issues

---

## 🗂 Recommended Folder Structure

```
Location-tracker-API/
│
├── fastapi/
├── flask/
├── node_express/
├── rust_actix/
├── docs/
│   └── Toolkit.md
│
└── docker-compose.yml
```