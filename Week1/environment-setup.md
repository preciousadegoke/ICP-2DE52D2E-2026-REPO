
# Week 1 — Development Environment Setup

## DevOps Engineering Self-Learning Internship

**Intern:** Precious Adegoke  
**Organization:** InternCareerPath  
**Program:** DevOps Engineering Self-Learning Internship  
**Environment:** Windows + WSL2 (Ubuntu)

---

## 1. Overview

This document describes the development environment prepared for the DevOps Engineering internship.

The environment was configured to support the two selected internship projects:

1. CI/CD Pipeline
2. Infrastructure as Code

The setup provides tools for Linux administration, source control, containerization, CI/CD development, infrastructure provisioning, scripting, and GitHub integration.

---

## 2. Operating Environment

The primary development environment is Ubuntu running through Windows Subsystem for Linux 2 (WSL2).

### Verified Environment

| Component | Configuration |
|---|---|
| Linux Distribution | Ubuntu 24.04.1 LTS |
| WSL Version | WSL2 |
| Kernel | 6.18.33.2-microsoft-standard-WSL2 |
| Shell | Bash |
| Init System | systemd |
| Architecture | x86_64 |

The operating system was verified using:

```bash
cat /etc/os-release
uname -r
```

WSL provides a Linux development environment while allowing integration with the Windows host system.

---

## 3. Git

Git is used for source control and change tracking throughout the internship.

**Installed Version:**

```text
git version 2.43.0
```

The following global configuration was established:

```text
User Name: Precious Adegoke
Default Branch: main
```

Verification commands:

```bash
git --version
git config --global user.name
git config --global init.defaultBranch
```

Before creating the official internship repository, Git fundamentals were practised in a separate Linux lab repository.

Exercises included:

- Repository initialization
- Staging and committing
- Branch creation
- Feature branches
- Fast-forward merging
- Merge conflicts
- Manual conflict resolution
- `.gitignore`
- `git diff`
- `git restore`
- `git restore --staged`
- Git history inspection

---

## 4. Docker

Docker is used to package applications into containers and will support the CI/CD project.

**Docker Version:**

```text
Docker version 29.7.2
```

**Docker Compose Version:**

```text
Docker Compose version v5.5.1
```

The Docker daemon was verified using:

```bash
docker info
```

A complete image pull and container execution test was performed using:

```bash
docker pull hello-world
docker run --rm hello-world
```

The container completed successfully and returned:

```text
Hello from Docker!
```

This verified communication between the Docker CLI and Docker daemon, image retrieval from Docker Hub, container creation, and container execution.

A temporary network timeout occurred during the initial Docker Hub request. A subsequent image pull completed successfully.

---

## 5. Terraform

Terraform will be used for the Infrastructure as Code project.

**Installed Version:**

```text
Terraform v1.16.4
on linux_amd64
```

Terraform was installed using the HashiCorp APT repository.

Verification command:

```bash
terraform --version
```

Terraform will later be used to define infrastructure using version-controlled configuration files.

---

## 6. Python

Python is available for scripting, application development, testing, and automation.

**Installed Version:**

```text
Python 3.12.3
```

Verification command:

```bash
python3 --version
```

Python may be used to provide a lightweight application for demonstrating automated testing, containerization, and CI/CD processes.

---

## 7. GitHub CLI

GitHub CLI is installed to support interaction with GitHub from the terminal.

**Installed Version:**

```text
gh version 2.45.0
```

Verification command:

```bash
gh --version
```

GitHub authentication will be configured separately when the internship repository is connected to GitHub.

---

## 8. Visual Studio Code

Visual Studio Code is available as the primary code editor.

**Installed Version:**

```text
1.138.0
```

Verification command:

```bash
code --version
```

VS Code can be launched from the WSL environment and used to edit files stored within the Linux filesystem.

---

## 9. Linux Fundamentals Practised

Before beginning the selected projects, practical Linux exercises were completed covering:

- Files and directories
- File permissions
- Bash commands
- Shell scripting
- Processes and background jobs
- Process termination and signals
- systemd and service inspection
- Networking interfaces
- Routing
- DNS resolution
- HTTP connectivity
- Listening ports
- Package management
- Environment variables
- Application logs
- System logs using `journalctl`

A Bash system-information script was also created during the Linux lab.

---

## 10. Environment Validation Summary

| Tool / Component | Status |
|---|---|
| WSL2 | Verified |
| Ubuntu Linux | Verified |
| Bash | Verified |
| systemd | Verified |
| Git | Verified |
| Docker CLI | Verified |
| Docker Engine | Verified |
| Docker Compose | Verified |
| Docker container execution | Verified |
| Terraform | Verified |
| Python | Verified |
| GitHub CLI | Verified |
| Visual Studio Code | Verified |

The development environment is prepared for the implementation stages of the internship.

---

## 11. Challenges Encountered

### 11.1 HashiCorp Repository Signing

During Terraform setup, APT initially reported that the HashiCorp repository signing key could not be verified.

The repository signing-key configuration was corrected before continuing with the installation.

### 11.2 Package Download Timeout

The Terraform package download initially timed out while connecting to the HashiCorp package repository. Retrying the installation successfully completed the download.

### 11.3 Docker Hub Timeout

The first attempt to execute the Docker `hello-world` container timed out while contacting Docker Hub.

The registry hostname resolved successfully, and a subsequent:

```bash
docker pull hello-world
```

completed successfully.

Running the container afterward confirmed that Docker was functioning correctly.

These issues provided practical experience in distinguishing installation problems from repository-authentication and network-connectivity problems.

---

## 12. Conclusion

The Week 1 environment setup established a functional Linux-based DevOps development environment using WSL2.

The required tools for version control, containerization, scripting, GitHub integration, CI/CD development, and Infrastructure as Code have been installed and verified.

This environment will serve as the foundation for the remaining internship tasks.
