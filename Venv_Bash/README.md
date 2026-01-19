# Virtual Environment & Bash Automation

## Tasks Overview
This folder contains scripts for managing Python environments and Bash shell automation, satisfying criteria Pv1, Pv2, and the Bash requirement.

### Included Files
* **Pv1 - `Pv1_setup.sh`**: A shell script demonstrating the commands to create a Python Virtual Environment (`venv`).
* **Bash - `Bash_api_check.sh`**: A Bash automation script that:
    1. Uses `curl` to check the HTTP status code of a target API.
    2. Logs the result (Success/Failure) to a log file.
    3. Conditionally executes further logic based on reachability.

### Usage
```bash
chmod +x *.sh
./Pv1_setup.sh
./Bash_api_check.sh