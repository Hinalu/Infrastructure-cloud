# Jenkins CI/CD

## Tasks Overview
CI/CD Pipeline configuration (Criteria J1, J2).

### Included Files
* **`J2_Jenkinsfile`**: The pipeline definition script.

---

## 🎓 Exam Prep: Concepts & Explanations

### 1. What is CI/CD?
* **CI (Continuous Integration):** Automatically building and testing code every time a developer saves work.
* **CD (Continuous Deployment):** Automatically pushing that code to production servers.

### 2. What is a Pipeline?
A set of automated steps. In our `Jenkinsfile`, the steps are:
1.  **Prepare:** Get the code.
2.  **Build:** Create the Docker image.
3.  **Test:** Check if the web server works (using `curl`).

### 3. Why `agent any`?
This tells Jenkins it can run this job on any available computer (node) connected to the Jenkins system.