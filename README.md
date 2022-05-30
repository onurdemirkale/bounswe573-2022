# Introduction
This is a repository for the course SWE.573. Throughout this semester, this project repository will be updated on a regular basis to reflect the changes made over time. Please refer to the wiki of this repository to learn more about the progress of this course, research made and lessons learned.

The purpose of this project is to develop is to create a web application for people who get a thrill from learning and sharing knowledge. The web application intends to create an environment for such like-minded people for the sake of learning.

# System Requirements

The system only requires the installation of Docker and Docker-Compose to run the Django application locally. Both can be installed on Docker.com.

Requirements:

Docker
Docker-Compose

# Running through Docker-Compose

To run the Django application through Docker-Compose, switch to the directory of the Docker-Compose file using the preferred command line tool and run the following commands:

docker-compose build

docker-compose up

Docker-Compose builds and starts a Docker image out of its current context and simultaneously starts a container running Postgres image as well. The networking between the containers are simplified and handled through Docker-Compose. Environment variables to connect the database and the Django application is specified in the Docker-Compose file.

During the development, it might be necessary to use the manage.py file to run various Django commands. To access the container while its running, run the following command:

docker exec -it ‘CONTAINER-ID’ bash

This command will start the bash inside the container and connect it to the standard input and output of the host operating system. The container ID can be obtained by running the following command:

docker ps

This command will list all running containers and allow the user to copy the container ID.

# Running using Dockerfile with an online database

To run the Django application by building an image out of its current context using a Dockerfile, first create an environment variables file with the name ‘.env’. This naming convention is not a necessity however this filename is included in the gitignore file and prevents the accidental push of credentials to the GitHub repository. A sample environments file can be found under the name .env.sampel. The contents of the environment variables file is specified in the credentials section (1.0) in the project report. Once the environment variables file is included in the Docker command as demonstrated below, the environment variables are injected into the Docker container and the Django application uses these variables to connect to the database and set various Django settings.

To run the Docker container, run the following commands:

docker build -t ‘YOUR-DOCKER-USERNAME’/‘TAG-NAME’ .

docker run —env-file .env ‘YOUR-DOCKER-USERNAME’/‘TAG-NAME’
