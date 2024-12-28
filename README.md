# Ml_Lab
# ML Project with Docker and Jenkins Pipeline

This repository contains a Machine Learning project that leverages Docker for containerization and Jenkins for continuous integration. The goal of this project is to build and deploy a machine learning model using Docker containers and automate the build and deployment process with Jenkins.

## Project Structure

- **Dockerfile**: Defines the environment to run the project in a Docker container.
- **requirements.txt**: Contains the necessary Python dependencies for the project.
- **Jenkinsfile**: Contains the Jenkins pipeline configuration for automating the build, run, and cleanup of the Docker container.
- **ML_Lab_Exam_(Aman_Kumar_Sinha).ipynb**: Jupyter Notebook containing the machine learning model and related code.
- **ml_lab_exam_(aman_kumar_sinha).py**: Python script for running the machine learning model.
- **README.md**: This file, which provides an overview of the project.

## Installation

### Prerequisites

- **Docker**: Ensure Docker is installed and running on your machine.
- **Jenkins**: Set up Jenkins for continuous integration.
- **Git**: You need Git to clone the repository.

### Steps to Run the Project Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/AmanSinha373/Ml_Lab.git
    cd Ml_Lab
    ```

2. Build the Docker image:
    ```bash
    docker build -t ml_project .
    ```

3. Run the Docker container:
    ```bash
    docker run -d --name ml_container ml_project
    ```

4. Clean up after running:
    ```bash
    docker rm -f ml_container
    docker rmi ml_project
    ```

### Jenkins Pipeline Setup

1. Create a new **Pipeline** job in Jenkins.
2. Under **Pipeline**, choose **Pipeline script from SCM** and configure it to use the Git repository where this `Jenkinsfile` is stored.
3. Run the Jenkins job to automatically build the Docker image, run the container, and clean up.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.


