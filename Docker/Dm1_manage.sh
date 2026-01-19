#!/bin/bash
# Task Dm1: Docker Management Script

echo "--- Stopping Containers ---"
docker stop apache-skills-test
docker stop my-alpine-app 2>/dev/null

echo "--- Removing Containers ---"
docker rm apache-skills-test
docker rm my-alpine-app 2>/dev/null

echo "--- Removing Images ---"
docker rmi my-apache-app
docker rmi my-alpine-app

echo "--- Cleanup Complete ---"