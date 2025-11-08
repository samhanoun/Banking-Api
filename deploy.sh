#!/bin/bash

# Check if the IMAGE_NAME environment variable is set
if [ -z "$IMAGE_NAME" ]; then
  echo "Error: IMAGE_NAME environment variable is not set."
  exit 1
fi

# Pull the latest image from Docker Hub
docker pull $IMAGE_NAME:latest

# Stop and remove the old container
docker stop $IMAGE_NAME
docker rm $IMAGE_NAME

# Run the new container
docker run -d -p 80:80 --name $IMAGE_NAME $IMAGE_NAME:latest
