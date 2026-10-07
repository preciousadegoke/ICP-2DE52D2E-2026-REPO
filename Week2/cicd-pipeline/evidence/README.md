# Week 2 — CI/CD Pipeline Evidence

This directory contains supporting evidence for the CI/CD Pipeline implemented during **Week 2** of the InternCareerPath DevOps Engineering Internship.

The evidence demonstrates that the pipeline can automatically test the application, build and verify its Docker image, detect a regression, prevent dependent pipeline stages from proceeding after a test failure, and successfully recover after the problem is corrected.

---

## Evidence 1 — Successful CI Pipeline

### Description

The first stage of validation confirmed that the CI pipeline could successfully process a correct version of the application.

The GitHub Actions workflow was automatically triggered by a push to the `main` branch.

The pipeline executed two dependent jobs:

1. **Run Automated Tests**
2. **Build and Verify Docker Image**

The Docker job was configured to execute only after the automated test job completed successfully.

### Pipeline Flow

```text
Push to main
     |
     v
Run Automated Tests
     |
     | PASS
     v
Build Docker Image
     |
     v
Start Container
     |
     v
Verify /health Endpoint
     |
     v
Pipeline Success
```

### Evidence

![Successful CI Pipeline](./screenshots/01-successful-ci-pipeline.JPG)

### Result

The workflow completed successfully.

The automated testing job verified the Python application using `pytest`, while the Docker job:

- Built the application image
- Started a container from the image
- Exposed the application on port `5000`
- Checked the `/health` endpoint
- Confirmed that the application was healthy
- Collected container logs
- Stopped the test container

**Status:** Passed

---

## Evidence 2 — CI Regression Detection

### Description

A controlled failure test was performed to verify that the CI pipeline could detect a regression before an incorrect change was merged into the `main` branch.

A temporary branch named:

```text
test/ci-failure-demo
```

was created.

The expected HTTP status code in the health endpoint test was intentionally changed from the correct value:

```python
assert response.status_code == 200
```

to an incorrect value:

```python
assert response.status_code == 500
```

The change was submitted through a pull request targeting `main`.

### Expected Behaviour

The automated test stage was expected to fail because the `/health` endpoint correctly returned HTTP `200`, while the modified test incorrectly expected HTTP `500`.

Because the Docker job depends on the test job, the later Docker validation stage was not allowed to proceed after the automated tests failed.

### Pipeline Flow

```text
Pull Request
     |
     v
Run Automated Tests
     |
     X FAIL
     |
     v
Regression Detected
     |
     X
Docker Validation Blocked
```

### Evidence

![CI Failure Detection](./screenshots/02-ci-failure-detection.JPG)

### Result

The CI pipeline successfully detected the intentionally introduced regression.

This demonstrated that the workflow does not simply build every submitted change. It first validates the application through automated testing and prevents dependent stages from proceeding when those tests fail.

The intentionally failing change was **not merged into `main`**.

**Status:** Regression successfully detected

---

## Evidence 3 — CI Recovery

### Description

After confirming that the CI pipeline could detect the regression, the incorrect test assertion was restored to the expected HTTP `200` status code.

The automated tests were executed locally again and both tests passed before the corrected branch was pushed.

The updated pull request then passed the CI validation process.

### Recovery Flow

```text
Regression Detected
     |
     v
Correct Test Assertion
     |
     v
Run Local Tests
     |
     | PASS
     v
Push Correction
     |
     v
GitHub Actions
     |
     +----> Automated Tests PASS
     |
     +----> Docker Verification PASS
     |
     v
Pipeline Recovered
```

### Evidence

![CI Recovery](./screenshots/03-ci-recovery.JPG)

### Result

After the correction:

- The automated test job passed.
- The Docker image was built successfully.
- The container started successfully.
- The application health check passed.
- The complete workflow returned to a successful state.

The demonstration pull request was used only for CI validation and was not merged into `main`.

**Status:** Recovery verified

---

## CI/CD Validation Summary

| Validation | Purpose | Result |
|---|---|---|
| Local automated testing | Verify application behaviour before CI execution | Passed |
| Local Docker build | Verify container image creation | Passed |
| Local container execution | Verify the application runs inside Docker | Passed |
| Health endpoint verification | Verify application availability | Passed |
| GitHub Actions test job | Automatically execute tests after repository changes | Passed |
| Docker CI job | Build and validate the application container automatically | Passed |
| Controlled regression | Verify that CI detects incorrect application expectations | Detected |
| Job dependency | Prevent Docker validation after failed tests | Verified |
| Recovery validation | Verify successful pipeline execution after correction | Passed |

---

## Technologies Demonstrated

The Week 2 CI/CD implementation currently demonstrates practical use of:

- Git
- GitHub
- GitHub Actions
- Python
- Flask
- pytest
- Docker
- Gunicorn
- Bash/Linux
- HTTP health checks
- Pull request validation
- Automated regression detection

---

## Conclusion

The Week 2 CI/CD validation demonstrated both the successful and failure paths of an automated software delivery workflow.

Rather than validating only a successful build, the exercise confirmed that the pipeline can detect an incorrect change, stop dependent processing after test failure, and return to a successful state after the issue is corrected.

This provides evidence that the CI workflow functions as an automated quality gate for changes to the application.
