# Docker Containerization

## Tasks Overview
This folder contains Dockerfiles and management scripts satisfying criteria Di1-Di3, Dc1, and Dm1.

### Included Files
* **Di2 - `Di2_Dockerfile`**: (Task 3) Ubuntu-based Apache image listening on port 8088 with `mod_rewrite` enabled.
* **Di3 - `Di3_Dockerfile_alpine`**: (Experiment 2) Lightweight Alpine Nginx image serving the same content.
* **Dc1 - `Dc1_build_run.sh`**: Bash script to build the images and run the containers.
* **Dm1 - `Dm1_manage.sh`**: Bash script to stop and remove containers/images.
* **`files/index.html`**: The custom landing page required by the Skills Exam.

### Usage
1. Make scripts executable:
   ```bash
   chmod +x *.sh