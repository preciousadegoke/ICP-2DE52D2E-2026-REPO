# Week 2 — CI/CD Pipeline Project

## Overview

This project implements a complete Continuous Integration and Continuous Delivery (CI/CD) workflow as part of Week 2 of the InternCareerPath DevOps Engineering Internship.

A lightweight Python/Flask application is automatically tested, containerized, verified, and delivered as a Docker image through GitHub Actions.

Successful changes pushed to the `main` branch produce a versioned container artifact that is published to GitHub Container Registry (GHCR).

The delivered image was also independently retrieved from GHCR, executed locally, and verified through its HTTP health endpoint.

---

## Project Objectives

The objectives of this project are to:

- Build a lightweight Python web application.
- Create automated tests using pytest.
- Package the application with Docker.
- Run the application with Gunicorn.
- Implement Continuous Integration using GitHub Actions.
- Automatically validate pushes and pull requests.
- Prevent dependent jobs from proceeding after test failures.
- Verify container health before delivery.
- Demonstrate automated regression detection and recovery.
- Implement Continuous Delivery to GitHub Container Registry.
- Generate both convenient and source-traceable container tags.
- Restrict image publication to successful pushes to `main`.
- Verify the delivered registry artifact independently.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application runtime |
| Flask | Web application framework |
| pytest | Automated application testing |
| Gunicorn | Production WSGI application server |
| Docker | Application containerization |
| Git | Version control |
| GitHub | Remote repository and pull request management |
| GitHub Actions | CI/CD workflow automation |
| GitHub Container Registry | Container artifact registry |
| Bash/Linux | Development and verification environment |
| curl | HTTP endpoint and health verification |

---

## Application Endpoints

### Root Endpoint

```text
GET /
```

Returns application information confirming that the service is running.

Example response:

```json
{
  "message": "InternCareerPath CI/CD Pipeline",
  "status": "running"
}
```

### Health Endpoint

```text
GET /health
```

Returns:

```json
{
  "status": "healthy"
}
```

with HTTP status `200`.

The health endpoint is used during both local and automated container verification.

---

## Project Structure

```text
ICP-2DE52D2E-2026-REPO/
├── .github/
│   └── workflows/
│       └── cicd.yml
│
└── Week2/
    └── cicd-pipeline/
        ├── app/
        │   ├── __init__.py
        │   └── main.py
        ├── tests/
        │   ├── __init__.py
        │   └── test_app.py
        ├── evidence/
        │   ├── README.md
        │   └── screenshots/
        │       ├── 01-successful-ci-pipeline.JPG
        │       ├── 02-ci-failure-detection.JPG
        │       ├── 03-ci-recovery.JPG
        │       ├── 04-successful-cd-pipeline.JPG
        │       ├── 05-ghcr-published-image.JPG
        │       └── 06-ghcr-runtime-verification.JPG
        ├── .dockerignore
        ├── Dockerfile
        ├── README.md
        ├── requirements.txt
        └── requirements-dev.txt
```

GitHub Actions workflow files must be stored under:

```text
.github/workflows/
```

Therefore, the CI/CD workflow is maintained at repository level while the application itself remains inside the Week 2 project directory.

---

## Local Development

Create a Python virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install development dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

---

## Automated Testing

Run:

```bash
pytest -v
```

The automated tests validate:

- Root endpoint availability.
- Health endpoint availability.
- Expected HTTP status codes.
- Expected JSON responses.

The validated test suite produces:

```text
2 passed
```

---

## Docker Containerization

Build the application locally:

```bash
docker build -t icp-cicd-app:week2 .
```

Run it:

```bash
docker run --rm -d \
  --name icp-cicd-app \
  -p 5000:5000 \
  icp-cicd-app:week2
```

Verify the root endpoint:

```bash
curl -i http://localhost:5000/
```

Verify application health:

```bash
curl -i http://localhost:5000/health
```

Stop the container:

```bash
docker stop icp-cicd-app
```

---

## Container Design

The image uses:

```text
python:3.12-slim
```

as its base image.

Only production dependencies are installed inside the application image.

Gunicorn is used instead of Flask's development server for container execution.

The Dockerfile also creates an unprivileged application user and executes the application as that user rather than as root.

This reduces unnecessary privileges within the running container.

---

## GitHub Actions CI/CD Workflow

The workflow is defined in:

```text
.github/workflows/cicd.yml
```

It responds to relevant application or workflow changes on:

- Pushes to `main`.
- Pull requests targeting `main`.

The workflow consists of three dependent jobs:

```text
Run Automated Tests
        |
        v
Build and Verify Docker Image
        |
        v
Publish Docker Image to GHCR
```

The third job is conditional and publishes artifacts only for successful pushes to `main`.

---

## Job 1 — Automated Tests

The test job:

1. Checks out the repository.
2. Configures Python 3.12.
3. Restores or prepares the pip dependency cache.
4. Installs development dependencies.
5. Executes the pytest suite.

If the tests fail, dependent jobs do not proceed.

This makes automated testing the first quality gate in the pipeline.

---

## Job 2 — Docker Build and Runtime Verification

The Docker validation job depends on the successful completion of the test job.

It:

1. Checks out the repository.
2. Builds the application Docker image.
3. Starts a container from that image.
4. Maps the service to port `5000`.
5. Repeatedly checks the `/health` endpoint.
6. Fails if the application does not become healthy.
7. Collects container logs.
8. Stops the temporary verification container.

This verifies more than image compilation: the resulting image must successfully execute the application.

---

## Job 3 — Continuous Delivery to GHCR

The publish job depends on successful Docker verification.

It runs only when:

```text
event = push
branch = main
```

The job:

1. Checks out the repository.
2. Authenticates to GitHub Container Registry.
3. Generates Docker image metadata.
4. Builds the production container image.
5. Publishes the image to GHCR.

The resulting image is available as:

```text
ghcr.io/preciousadegoke/icp-cicd-app
```

---

## Container Tagging Strategy

Each successful delivery generates two tags.

### Latest Tag

```text
ghcr.io/preciousadegoke/icp-cicd-app:latest
```

This identifies the most recently delivered image.

### Commit SHA Tag

Example:

```text
ghcr.io/preciousadegoke/icp-cicd-app:sha-b74e219
```

The SHA-based tag provides traceability between the delivered artifact and the Git revision that produced it.

This makes it possible to identify or retrieve a specific delivered version rather than relying only on the mutable `latest` tag.

---

## Pipeline Architecture

```text
                         Source Change
                              |
                              v
                    Push / Pull Request
                              |
                              v
                       GitHub Actions
                              |
                              v
                    Automated pytest Tests
                              |
                         +----+----+
                         |         |
                       FAIL       PASS
                         |         |
                         v         v
                       STOP    Docker Build
                                   |
                                   v
                            Start Container
                                   |
                                   v
                             Health Check
                                   |
                              +----+----+
                              |         |
                            FAIL       PASS
                              |         |
                              v         v
                            STOP    Push to main?
                                      |
                                 +----+----+
                                 |         |
                                NO        YES
                                 |         |
                                 v         v
                           No Publication  GHCR Login
                                             |
                                             v
                                      Generate Metadata
                                             |
                                             v
                                       Build & Publish
                                             |
                                             v
                                   GitHub Container Registry
                                             |
                                        +----+----+
                                        |         |
                                      latest   sha-<commit>
```

---

## Pull Request Behaviour

Pull requests targeting `main` execute the validation stages of the workflow.

They can therefore run:

```text
Automated Tests
       |
       v
Docker Verification
```

but they do not publish a container image.

The publication condition prevents unmerged pull request code from replacing the delivered `latest` image.

---

## Regression Detection and Recovery

A controlled regression was introduced during validation by temporarily changing the expected HTTP status code in the health endpoint test.

The incorrect change caused the automated test job to fail.

Because the Docker job depends on the test job, Docker verification was prevented from proceeding after the failed test.

The assertion was subsequently corrected, local tests returned to a passing state, and the updated pull request successfully completed CI validation.

The intentionally failing change was not merged into `main`.

This demonstrated both failure detection and successful recovery.

---

## GHCR Authentication and Permissions

The workflow uses GitHub's automatically provided:

```text
GITHUB_TOKEN
```

for registry authentication.

No manually created long-lived Personal Access Token is stored in the repository for the publication job.

The workflow grants the permissions required for repository access and package publication:

```yaml
permissions:
  contents: read
  packages: write
```

This provides the workflow with the package-write capability required to publish container artifacts to GHCR.

---

## Delivered Artifact Verification

After successful publication, the delivered image was independently retrieved from GitHub Container Registry.

The published image was executed using:

```bash
docker run --rm -d \
  --name icp-cicd-app-ghcr \
  -p 5000:5000 \
  ghcr.io/preciousadegoke/icp-cicd-app:latest
```

The root endpoint returned HTTP `200` and:

```json
{
  "message": "InternCareerPath CI/CD Pipeline",
  "status": "running"
}
```

The health endpoint also returned HTTP `200` with:

```json
{
  "status": "healthy"
}
```

Gunicorn started successfully with two workers inside the delivered container.

This independently verified that the artifact stored in GHCR was executable and healthy after delivery.

---

## Continuous Integration vs Continuous Delivery

This project implements both CI and Continuous Delivery.

### Continuous Integration

The CI portion automatically:

- Tests application behaviour.
- Builds the container image.
- Executes the resulting container.
- Verifies application health.
- Detects regressions.
- Blocks dependent processing when validation fails.

### Continuous Delivery

The delivery portion automatically:

- Runs only after successful CI validation.
- Authenticates to the container registry.
- Creates traceable image metadata.
- Builds the deliverable image.
- Publishes it to GHCR.
- Maintains `latest` and commit-specific image tags.

The project currently implements **Continuous Delivery rather than automatic production deployment**.

A successful change to `main` produces a deployable registry artifact, but the workflow does not automatically modify a live production environment.

---

## Evidence

Detailed implementation evidence is maintained in:

[Week 2 CI/CD Evidence](./evidence/README.md)

The evidence includes:

1. Successful CI execution.
2. Controlled CI regression detection.
3. Successful CI recovery.
4. Successful complete CI/CD workflow execution.
5. GHCR container publication.
6. Independent execution and health verification of the delivered artifact.

---

## Security and Reliability Decisions

Several design decisions improve the reliability and security of the workflow:

- Tests must succeed before Docker verification.
- Docker verification must succeed before publication.
- Pull requests cannot publish the `latest` image.
- Publication is restricted to pushes to `main`.
- Registry authentication uses `GITHUB_TOKEN`.
- The workflow uses explicit package permissions.
- The container runs as an unprivileged user.
- Runtime health is verified before delivery.
- Container logs are collected even when verification fails.
- Cleanup steps use `if: always()` so the temporary CI container is stopped even after failures.
- SHA-based tags provide artifact traceability.
- The Ubuntu runner is pinned to `ubuntu-24.04` rather than relying on a moving `ubuntu-latest` target.

---

## Final Outcome

The Week 2 CI/CD project successfully implements an automated software validation and delivery pipeline.

The completed workflow can:

- Detect repository changes.
- Execute automated tests.
- Detect regressions.
- Prevent downstream processing after test failure.
- Build a Docker application image.
- Execute and health-check the container.
- Publish verified images to GitHub Container Registry.
- Generate `latest` and source-traceable SHA tags.
- Prevent pull requests from publishing delivery artifacts.
- Retrieve and independently execute the delivered registry image.

The project therefore demonstrates the complete path from source-code change to a tested, containerized, traceable, registry-hosted, and independently verified software artifact.
