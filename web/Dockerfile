# see https://hub.docker.com/search for more base images.

# This looks like a Dockerfile, which is used to create a Docker container. 
# Docker is a tool that helps you create, deploy, and run applications 
# inside containers.


# This is specifying the base image for your container. 
# In this case, it's using an official Python image with version 3.9 
# from Docker Hub.
FROM python:3.9


# It's just a piece of metadata.
MAINTAINER Deem Alowairdhi "411214706@qu.edu.sa"


# RUN: This command lets Docker know that the following command should be 
# run in the container during the build process.


# This updates the list of available packages in the container.
RUN apt-get update -y

# This installs the specified packages.
RUN apt-get install -y python3-pip python3-dev build-essential


# This command copies the current directory (where your Dockerfile is) 
#into the /app directory in the container.
COPY . /app

# This sets the working directory inside the container to /app. 
# Future commands will be run from this directory.
WORKDIR /app


# This installs the Python packages listed in requirements.txt. 
# This file typically contains a list of packages and their versions that your application needs to run.
RUN pip install -r requirements.txt

# ENTRYPOINT: This sets the default application that will be executed 
# when the container starts.
ENTRYPOINT ["python3"]

# CMD: This provides default arguments to the ENTRYPOINT. 
# In this case, when the container starts, it will run python3 app.py.
CMD ["app.py"]
