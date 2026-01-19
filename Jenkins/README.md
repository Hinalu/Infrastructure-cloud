# Jenkins CI/CD

## Tasks Overview
This folder contains the Pipeline configuration for automating the build and test process, satisfying criteria J1 and J2.

### Included Files
* **J2 - `J2_Jenkinsfile`**: A Declarative Pipeline script defining 3 stages:
    1. **Prepare**: Checks out source code.
    2. **Build**: Builds the Docker image using the Dockerfile from the `Docker/` folder.
    3. **Test**: Runs the container and performs a `curl` connectivity check.

### Usage
1. Create a new "Pipeline" job in Jenkins.
2. In the "Pipeline Definition", choose "Pipeline script from SCM".
3. Point it to this GitHub repository and specify the Script Path as `Jenkins/J2_Jenkinsfile`.