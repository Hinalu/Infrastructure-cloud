#!/bin/bash
# Task Dc1: Build and Run Script

echo "--- Building Apache Image (Task 3) ---"
docker build -t my-apache-app -f Di2_Dockerfile .

echo "--- Running Apache Container on Port 8088 ---"
# Maps host port 8088 to container port 8088
docker run -d -p 8088:8088 --name apache-skills-test my-apache-app

echo "--- Building Alpine Image (Experiment 2) ---"
docker build -t my-alpine-app -f Di3_Dockerfile_alpine .

echo "--- Verifying Running Containers ---"
docker ps