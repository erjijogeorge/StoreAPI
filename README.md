<h1 align="center">StoreAPI
</h1>

<p align="center">
  <a href="https://github.com/erjijogeorge/StoreAPI/actions/workflows/python-app.yml">
    <img src="https://github.com/erjijogeorge/StoreAPI/actions/workflows/python-app.yml/badge.svg?branch=master" alt="GitHub Actions Build">
  </a>
  <a href="https://sonarcloud.io/summary/new_code?id=devsquad_githubsonar">
    <img src="https://sonarcloud.io/api/project_badges/measure?project=devsquad_githubsonar&metric=alert_status" alt="Quality Gate Status">
  </a>
</p>

# Analyze your code for free with SonarCloud 

This SonarSource project, available as a GitHub Action, scans your projects with SonarCloud, and helps developers produce 
<p align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=devsquad_githubsonar">
    <img src="https://sonarcloud.io/images/project_badges/sonarcloud-white.svg" alt="SonarCloud" width="150">
  </a>
  <a href="https://sonarcloud.io/summary/new_code?id=devsquad_githubsonar">
    <img src="https://sonarcloud.io/api/project_badges/quality_gate?project=devsquad_githubsonar" alt="Quality Gate" width="150">
  </a>
</p>

[SonarCloud](https://www.sonarsource.com/products/sonarcloud/) is a widely used static analysis solution for continuous code quality and security inspection. 
It helps developers identify and fix issues in their code that could lead to bugs, vulnerabilities, or decreased development velocity.
SonarCloud supports the most popular programming languages, including Java, JavaScript, TypeScript, C#, Python, C, C++, and [many more](https://www.sonarsource.com/knowledge/languages/).

## Introduction

StoreAPI is a robust and scalable RESTful API built with FastAPI. This project aims to provide a solid foundation for managing store operations, including product listings, inventory management, and order processing.

## Features

- **FastAPI**: Utilizes FastAPI for building high-performance APIs with automatic interactive documentation.
- **Authentication**: Includes JWT-based authentication.
- **Database Integration**: Supports SQL databases with SQLAlchemy.
- **Automated Testing**: Uses pytest for testing.
- **Continuous Integration**: Integrated with GitHub Actions for CI/CD.
- **Code Quality**: Monitored by SonarCloud for maintaining high code quality.

## Getting Started

### Prerequisites

- Python 3.11.3+
- Docker (optional, for containerization)

### Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/erjijogeorge/StoreAPI.git
   cd StoreAPI
