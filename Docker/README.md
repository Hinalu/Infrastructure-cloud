# Docker Containerization

## Tasks Overview
Dockerfiles and management scripts (Criteria Di1-Di3, Dc1, Dm1).

### Included Files
* **`Di2_Dockerfile`**: Instructions to build the Apache image.
* **`Dc1_build_run.sh`**: Script to build and run containers.

---

## 🎓 Exam Prep: Concepts & Explanations

### 1. Container vs. Virtual Machine (VM)
* **VM:** Virtualizes the *Hardware*. Runs a full OS (heavy, slow boot).
* **Container:** Virtualizes the *OS (Kernel)*. Shares the host OS but isolates the application (lightweight, fast boot).

### 2. Image vs. Container
* **Image:** The "Recipe" or "Blueprint". It is read-only. (Defined by the Dockerfile).
* **Container:** The "Cake" or "Running Instance". It is the image brought to life.

### 3. Key Dockerfile Commands
* `FROM`: The base OS (e.g., Ubuntu).
* `RUN`: Executes commands during the build (installing software).
* `COPY`: Moves files from your laptop into the image.
* `CMD`: The command that runs when the container starts.

### 4. Port Mapping (`-p 8088:8088`)
Containers are isolated. The outside world cannot reach them by default.
* `-p HostPort:ContainerPort` creates a tunnel. It says "Traffic hitting port 8088 on my laptop should go to port 8088 inside the container."