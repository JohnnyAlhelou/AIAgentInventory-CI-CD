# AI Inventory Agent — CI/CD Pipeline

**EECE 430 | Assignment 6**

An AI-powered inventory management application built with Django and integrated with Google's Gemini API. This project implements a complete CI/CD pipeline using GitHub Actions, Docker, GitHub Container Registry (GHCR), and a self-hosted macOS runner.

## Project Structure

| File / Directory | Description |
|---|---|
| `chat/` | Django application, AI Agent, inventory models, and user interface |
| `config/` | Django project configuration and settings |
| `manage.py` | Django management commands |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Docker image configuration |
| `.dockerignore` | Files excluded from Docker builds |
| `.gitignore` | Files excluded from Git tracking |
| `.env.example` | Example environment configuration |
| `.github/workflows/ci.yml` | GitHub Actions CI/CD workflow |

## CI/CD Pipeline

The pipeline runs automatically whenever changes are pushed to the `main` branch.

**1. Test Django Application (CI)**

- Set up Python 3.12
- Install project dependencies
- Check Django configuration
- Run automated tests

**2. Build and Publish Docker Image (CI)**

- Build a Linux AMD64 Docker image
- Authenticate with GitHub Container Registry
- Publish the image with the `latest` tag

**3. Verify Mac Deployment Runner (CD)**

- Connect to the self-hosted macOS ARM64 runner
- Verify Docker is available and running

**4. Deploy AI Inventory Agent (CD)**

- Pull the latest Docker image from GHCR
- Replace the previously deployed container
- Preserve the SQLite database using a Docker volume
- Verify the application responds successfully

## Quick Navigation

- [GitHub Actions — Workflow Runs](https://github.com/JohnnyAlhelou/AIAgentInventory-CI-CD/actions)
- [CI/CD Workflow Configuration](.github/workflows/ci.yml)
- [Dockerfile](Dockerfile)
- [AI Agent Implementation](chat/agent.py)
- [Inventory Models](chat/models.py)
- [Automated Tests](chat/tests.py)
- [Django Settings](config/settings.py)
- [GitHub Repository](https://github.com/JohnnyAlhelou/AIAgentInventory-CI-CD)

## Running Locally

**Requirements:** Python 3.12, pip, and Docker Desktop for containerized deployment.

Create a Python virtual environment and install the dependencies:

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`

Configure the local `.env` file with the required Django environment variables.

Run the application:

`python manage.py migrate`

`python manage.py runserver`

Open `http://127.0.0.1:8000/`.

To run the automated tests:

`python manage.py test`

## Docker Deployment

The CI/CD pipeline publishes the Docker image to:

`ghcr.io/johnnyalhelou/aiagentinventory-ci-cd:latest`

The self-hosted runner deploys the application locally at:

`http://127.0.0.1:8001/`

The deployed application is accessible while the MacBook and Docker environment are running. It is not publicly hosted.

## Security

- API keys and Django secrets are stored in environment variables.
- The `.env` file is excluded from Git.
- GitHub Actions uses `GITHUB_TOKEN` for container registry authentication.
- SQLite data is stored in a persistent Docker volume during deployment.

**Note:** The web interface and CI/CD pipeline have been verified. AI chat functionality requires a valid Gemini API key and is not covered by the current automated test.

## CI/CD Verification

The pipeline has been successfully tested through an interface update from the original Inventory Agent to **Inventory Agent - CI/CD Version 2**.

The update was automatically tested, built, published, and deployed through GitHub Actions without manually restarting the deployed application.

## Assignment Information

**Course:** EECE 430

**Assignment:** 6 — AI Agent CI/CD

**Repository:** https://github.com/JohnnyAlhelou/AIAgentInventory-CI-CD
