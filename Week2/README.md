# Week 2 — CI/CD Pipeline

## Overview

Week 2 of the InternCareerPath DevOps Engineering Internship focuses on implementing and validating a practical Continuous Integration and Continuous Delivery (CI/CD) workflow.

The project uses a Python Flask application, automated testing with pytest, Docker containerization, GitHub Actions, and GitHub Container Registry (GHCR) to demonstrate the complete path from source-code validation to delivery of a runnable container artifact.

## Project

### CI/CD Pipeline

**Status:** Completed

Project directory:

```text
Week2/cicd-pipeline/
```

The completed implementation includes:

- Python Flask application with root and health endpoints.
- Automated pytest test suite.
- Docker containerization.
- Gunicorn application server.
- Non-root container execution.
- GitHub Actions Continuous Integration.
- Automated test execution.
- Automated Docker build and runtime verification.
- Container health checks.
- Controlled CI failure and recovery testing.
- Dependent-job failure protection.
- Continuous Delivery to GitHub Container Registry.
- `latest` and commit-SHA Docker image tagging.
- Main-branch-only artifact publication.
- Independent runtime verification of the delivered GHCR image.
- Documented implementation evidence with screenshots.

## CI/CD Flow

```text
Source Change
     |
     v
GitHub Actions
     |
     v
Automated Tests
     |
     v
Docker Build
     |
     v
Container Runtime Verification
     |
     v
Successful Push to main
     |
     v
GitHub Container Registry
     |
     v
Runnable Docker Artifact
```

Pull requests execute the validation stages but do not publish delivery artifacts.

## Container Artifact

The delivered container image is published as:

```text
ghcr.io/preciousadegoke/icp-cicd-app
```

The delivery process creates both a `latest` tag and a commit-specific SHA tag for traceability.

## Documentation

Detailed technical documentation:

[CI/CD Pipeline Project](./cicd-pipeline/README.md)

Implementation and validation evidence:

[CI/CD Evidence](./cicd-pipeline/evidence/README.md)

## Week 2 Outcome

Week 2 demonstrates a functioning CI/CD pipeline in which application changes are automatically tested, containerized, runtime-verified, and, after successful validation on `main`, published as traceable Docker artifacts to GitHub Container Registry.

The delivered registry image was independently executed and health-checked, confirming that the artifact produced by the pipeline is usable beyond the CI environment.
