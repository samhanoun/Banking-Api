#!/bin/bash

# Get the image name from the GitHub repository name
IMAGE_NAME=$(echo ${{ github.repository }} | tr '[:upper:]' '[:lower:]')

# Pull the latest image from Docker Hub
docker pull $IMAGE_NAME:latest

# Stop and remove the old container
docker stop $IMAGE_NAME
docker rm $IMAGE_NAME

# Run the new container
docker run -d -p 80:80 --name $IMAGE_NAME $IMAGE_NAME:latest
