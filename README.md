# Banking API

A simple API to manage banks, clients, and accounts.

## Project Overview

This project is a simple banking API built with FastAPI. It allows you to create and manage banks, clients, and accounts. You can also perform transactions, such as deposits and withdrawals, and view the transaction history of an account.

## Getting Started

To get started with the project, you'll need to have Python 3.12 and Docker installed on your machine.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    uvicorn main:api --reload
    ```

### Running with Docker

You can also run the application with Docker:

1.  Set the `IMAGE_NAME` environment variable:
    ```bash
    export IMAGE_NAME=your-docker-hub-username/your-repo-name
    ```
2.  Build the Docker image:
    ```bash
    docker build -t $IMAGE_NAME:latest .
    ```
3.  Run the Docker container:
    ```bash
    docker run -d -p 80:80 --name $IMAGE_NAME $IMAGE_NAME:latest
    ```

## API Guide

The API is documented with Swagger UI. You can access the documentation at `http://localhost:80/docs`.

### Banks

*   `POST /api/bank/new`: Create a new bank.
*   `GET /api/bank`: Get all banks.

### Clients

*   `POST /api/bank/{bank_id}/client`: Create a new client for a bank.
*   `GET /api/client/{client_id}`: Get a client by ID.
*   `PUT /api/client/{client_id}`: Update a client by ID.
*   `DELETE /api/client/{client_id}`: Delete a client by ID.

### Accounts

*   `POST /api/account/{account_id}/deposit`: Deposit money into an account.
*   `POST /api/account/{account_id}/withdraw`: Withdraw money from an account.
*   `GET /api/account/{account_id}/transactions`: Get the transaction history of an account.

## CI/CD Pipeline

The project includes a CI/CD pipeline that is triggered on every push and pull request to the `main` branch.

### CI Pipeline

The CI pipeline is defined in `.github/workflows/ci.yml`. It performs the following steps:

1.  Sets up Python 3.12.
2.  Installs the project dependencies.
3.  Lints the code with `flake8`.
4.  Runs the tests with `pytest`.

### CD Pipeline

The CD pipeline is defined in `.github/workflows/cd.yml`. It performs the following steps:

1.  Logs in to Docker Hub.
2.  Builds a Docker image of the application.
3.  Pushes the Docker image to a container registry.

To use the CD pipeline, you'll need to add the following secrets to your GitHub repository:

*   `DOCKER_HUB_USERNAME`: Your Docker Hub username.
*   `DOCKER_HUB_PASSWORD`: Your Docker Hub password.

### Self-Hosted Runner on WSL

To run the CD pipeline, you'll need to set up a self-hosted runner on your WSL environment.

1.  Follow the instructions in the [GitHub documentation](https://docs.github.com/en/actions/hosting-your-own-runners/adding-self-hosted-runners) to add a new self-hosted runner.
2.  When prompted, select `Linux` as the operating system and `x64` as the architecture.
3.  Follow the instructions to download, configure, and run the runner.

### Deployment

To deploy the application, you can use the `deploy.sh` script. This script will pull the latest image from the container registry and run it as a Docker container.

1.  Set the `IMAGE_NAME` environment variable:
    ```bash
    export IMAGE_NAME=your-docker-hub-username/your-repo-name
    ```
2.  Run the deployment script:
    ```bash
    ./deploy.sh
    ```
