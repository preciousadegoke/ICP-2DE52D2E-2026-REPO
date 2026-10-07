# Week 2 — CI/CD Pipeline Project

## Overview

This project implements a Continuous Integration pipeline as part of Week 2 of the InternCareerPath DevOps Engineering Internship.

The project demonstrates how application testing, containerization, health verification, and regression detection can be automated using GitHub Actions.

The application itself is intentionally lightweight so that the primary focus remains on the DevOps workflow and CI/CD practices.

---

## Project Objectives

The objectives of this project are to:

- Build a lightweight Python web application.
- Create automated application tests using pytest.
- Package the application as a Docker container.
- Verify the container locally before automation.
- Implement Continuous Integration using GitHub Actions.
- Automatically validate pushes and pull requests.
- Prevent dependent pipeline stages from running after test failures.
- Verify application health after container startup.
- Demonstrate CI regression detection and recovery.
- Maintain supporting technical evidence.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application runtime |
| Flask | Lightweight web application framework |
| pytest | Automated application testing |
| Gunicorn | Production WSGI application server |
| Docker | Application containerization |
| Git | Source control |
| GitHub | Remote repository and pull request management |
| GitHub Actions | CI workflow automation |
| Bash/Linux | Development and validation environment |

---

## Application Endpoints

The application exposes two HTTP endpoints.

### Root Endpoint

```text
GET /
```

Returns basic information confirming that the application is running.

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

The health endpoint is also used by the CI pipeline to verify that the application starts correctly inside its Docker container.

---

## Project Structure

```text
cicd-pipeline/
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
│       └── 03-ci-recovery.JPG
├── .dockerignore
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

The GitHub Actions workflow is stored at the repository level:

```text
.github/workflows/cicd.yml
```

GitHub requires workflow definitions to be stored under `.github/workflows/`.

---

## Local Development

### Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### Install Development Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

---

## Automated Testing

Run the test suite with:

```bash
pytest -v
```

The test suite validates:

- The root application endpoint.
- The health endpoint.
- Expected HTTP status codes.
- Expected JSON responses.

A correct application currently produces:

```text
2 passed
```

---

## Docker Containerization

Build the application image:

```bash
docker build -t icp-cicd-app:week2 .
```

Run the container:

```bash
docker run --rm -d \
  --name icp-cicd-app \
  -p 5000:5000 \
  icp-cicd-app:week2
```

Verify the application:

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

The Docker image uses:

```text
python:3.12-slim
```

as its base image.

Only production dependencies are installed inside the image.

The application is executed using Gunicorn and runs as an unprivileged application user rather than as the container's root user.

This reduces unnecessary privileges within the running container.

---

## CI Workflow

The GitHub Actions workflow automatically runs for relevant changes made through:

- Pushes to `main`
- Pull requests targeting `main`

The workflow contains two primary jobs.

### Job 1 — Automated Tests

The first job:

1. Checks out the repository.
2. Configures Python 3.12.
3. Installs development dependencies.
4. Executes the pytest test suite.

If the tests fail, the pipeline does not proceed to the dependent Docker job.

### Job 2 — Docker Build and Verification

The second job runs only after the automated tests succeed.

It:

1. Checks out the repository.
2. Builds the Docker image.
3. Starts the application container.
4. Performs an HTTP health check.
5. Displays container logs.
6. Stops the temporary container.

---

## Pipeline Architecture

```text
Git Push / Pull Request
          |
          v
    GitHub Actions
          |
          v
  Automated Test Job
          |
     +----+----+
     |         |
   FAIL       PASS
     |         |
     v         v
 Pipeline   Docker Build
  Stops         |
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
        Failure    Success
```

---

## Regression Detection Test

A controlled CI failure test was performed using a temporary branch.

The health endpoint test was deliberately configured with an incorrect expected HTTP status code.

The change was submitted through a pull request.

GitHub Actions detected the failing test during the automated test job. Because the Docker job depends on the successful completion of the test job, Docker validation did not proceed.

The incorrect assertion was subsequently corrected and local testing returned to:

```text
2 passed
```

The updated pull request then successfully completed both CI jobs.

The intentionally failing pull request was not merged into `main`.

---

## CI Environment

The workflow currently uses:

```text
ubuntu-24.04
```

instead of `ubuntu-latest`.

Pinning the runner provides greater predictability by avoiding an unexpected operating-system migration when GitHub changes the environment associated with `ubuntu-latest`.

The workflow also uses current major versions of the required GitHub Actions.

---

## Evidence

Detailed evidence of the CI validation process is available in:

[Week 2 CI/CD Evidence](./evidence/README.md)

The evidence demonstrates:

- A successful CI pipeline.
- Detection of an intentionally introduced regression.
- Prevention of dependent Docker processing after test failure.
- Successful CI recovery after correction.

---

## Current Outcome

The project currently provides a functioning Continuous Integration workflow capable of automatically:

- Testing the Python application.
- Building the Docker image.
- Starting the container.
- Checking application health.
- Detecting regressions.
- Blocking dependent processing after test failure.
- Validating corrected changes.

This establishes the Continuous Integration foundation required for the remaining CI/CD implementation.
