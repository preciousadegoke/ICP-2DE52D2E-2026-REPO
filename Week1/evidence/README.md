# Week 1 — Evidence

This directory contains supporting evidence for the practical activities completed during **Week 1** of the InternCareerPath DevOps Engineering Internship.

The evidence demonstrates the setup and verification of the development environment used for the internship.

---

## Evidence 1 — GitHub Repository

### Description

The official internship repository, `ICP-2DE52D2E-2026-REPO`, was created and published on GitHub.

The repository is used to maintain:

- Weekly internship documentation
- Project implementation files
- Environment setup documentation
- Technical evidence
- Git commit history
- CI/CD and Infrastructure as Code work throughout the internship

### Evidence

![Week 1 GitHub Repository](./screenshots/week1-github-repository.jpg)

### Verification

The repository was initialized locally with Git, connected to GitHub, and pushed to the remote `main` branch.

The repository includes the Week 1 documentation and maintains a structured Git history using descriptive commit messages.

**Status:** Completed

---

## Evidence 2 — Docker Verification

### Description

Docker was installed and configured as part of the development environment for the CI/CD project.

Docker functionality was tested by retrieving the official `hello-world` image from Docker Hub and executing it as a container.

### Commands Used

```bash
docker pull hello-world
docker run --rm hello-world
```

### Evidence

![Docker Verification](./screenshots/week1-docker-verification.jpg)

### Result

The container executed successfully and returned:

```text
Hello from Docker!
```

This verified that:

- The Docker CLI could communicate with the Docker daemon.
- The Docker daemon was running successfully.
- Images could be retrieved from Docker Hub.
- Docker could create a container from an image.
- The container could execute successfully.
- Container output could be returned to the terminal.

A temporary network timeout occurred during the initial Docker Hub request. The image was subsequently pulled successfully and the container test completed.

**Status:** Completed

---

## Evidence 3 — Terraform Verification

### Description

Terraform was installed as the primary Infrastructure as Code tool for the internship.

It will be used during the Infrastructure as Code project to define and provision infrastructure using version-controlled configuration files.

### Verification Command

```bash
terraform --version
```

### Evidence

![Terraform Verification](./screenshots/week1-terraform-verification.jpg)

### Result

The installed Terraform environment returned:

```text
Terraform v1.16.4
on linux_amd64
```

This confirmed that Terraform was installed successfully and available within the WSL2 Ubuntu development environment.

**Status:** Completed

---

## Week 1 Evidence Summary

| Evidence | Purpose | Result |
|---|---|---|
| GitHub Repository | Verify creation and publication of the official internship repository | Completed |
| Docker | Verify image retrieval and container execution | Completed |
| Terraform | Verify Infrastructure as Code tooling installation | Completed |

---

## Related Documentation

Additional details about the Week 1 activities are available in:

- [Week 1 Overview](../README.md)
- [Project Selection](../project-selection.md)
- [Development Environment Setup](../environment-setup.md)

---

## Conclusion

The evidence collected during Week 1 confirms that the core development environment required for the internship was successfully established and tested.

The environment now provides the foundation required for the selected **CI/CD Pipeline** and **Infrastructure as Code** projects.
