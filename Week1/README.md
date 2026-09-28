# Week 1 — DevOps Foundations

## Overview

Week 1 focused on establishing the technical foundation required for the DevOps Engineering internship.

The primary areas covered were:

- Linux fundamentals
- Advanced Git usage
- Project selection
- Development environment setup
- Tool verification

## Linux Fundamentals

Practical Linux exercises covered:

- File and directory management
- File permissions
- Bash scripting
- Processes and background jobs
- Process termination
- systemd and service inspection
- Network interfaces and routing
- DNS resolution
- HTTP connectivity
- Listening ports
- Package management
- Environment variables
- Application and system logs

A separate Linux practice environment was used before beginning work in the official internship repository.

## Git Practice

Git exercises included:

- Repository initialization
- Staging
- Commits
- Branches
- Feature-branch workflows
- Fast-forward merges
- Three-way merges
- Merge conflicts
- Manual conflict resolution
- `.gitignore`
- `git diff`
- `git restore`
- `git restore --staged`
- Commit-history inspection

## Selected Projects

Two projects were selected for the internship:

1. **CI/CD Pipeline**
2. **Infrastructure as Code**

Further details are available in [`project-selection.md`](./project-selection.md).

## Environment Setup

The development environment includes:

- Ubuntu 24.04.1 LTS through WSL2
- Git
- Docker
- Docker Compose
- Terraform
- Python
- GitHub CLI
- Visual Studio Code

Docker container execution was successfully verified using the `hello-world` image.

Detailed setup and verification information is available in [`environment-setup.md`](./environment-setup.md).

## Week 1 Deliverables

- [x] Linux fundamentals practice
- [x] Advanced Git practice
- [x] Project Selection Document
- [x] Development Environment Setup
- [x] Tool verification
- [x] Repository published to GitHub

## Challenges and Learning

During environment setup, repository-signing and temporary network timeout issues were encountered while installing Terraform and testing Docker.

Troubleshooting these issues provided practical experience distinguishing between:

- Installation failures
- Package-repository authentication issues
- Network connectivity failures
- Application/runtime failures

## Outcome

Week 1 established a functional development environment and the foundational Linux and Git skills required for the implementation stages of the internship.
