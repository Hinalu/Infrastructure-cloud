# Virtual Environment & Bash

## Tasks Overview
Python environment setup and Bash scripting (Criterion Pv1, Task 7).

### Included Files
* **`Pv1_setup.sh`**: Sets up a Python venv.
* **`Bash_api_check.sh`**: Checks API availability.

---

## 🎓 Exam Prep: Concepts & Explanations

### 1. What is a Virtual Environment (venv)?
It is an isolated folder for a Python project.
* **Why?** It lets you install specific libraries (like `requests` version 2.0) for one project without breaking another project that needs version 1.0.

### 2. Bash Scripting Basics
* **`#!/bin/bash` (Shebang):** The first line. It tells the computer "Use the Bash program to interpret this file."
* **`chmod +x`:** "Change Mode + Executable". It turns a text file into a program you can run.
* **`curl -o /dev/null`:** Run curl but throw away the output (we only care about the status code).