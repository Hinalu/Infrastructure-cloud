# Ansible Automation

## Tasks Overview
Ansible playbooks for Network and Server configuration (Criteria An2, An3, As2, As3).

### Included Files
* **`ansible.cfg`**: Config file (defaults).
* **`hosts`**: Inventory file (list of IP addresses).
* **`An2_ios_facts.yml`**: Network playbook.
* **`As2_apache_install.yml`**: Server playbook.

---

## 🎓 Exam Prep: Concepts & Explanations

### 1. What is Ansible?
Ansible is an **Agentless** automation tool. It connects to devices via SSH, pushes the configuration, and then disconnects. It uses **YAML** for its code.

### 2. Key Components
* **Inventory (`hosts`):** A list of devices to manage, grouped by type (e.g., `[routers]`, `[webservers]`).
* **Playbook (`.yml`):** The script describing *what* to do.
* **Task:** A single action inside a playbook (e.g., "Install Apache").
* **Module:** The code that actually runs the task (e.g., `apt`, `ios_config`, `copy`).

### 3. What is Idempotency?
This is the most important concept in Ansible. It means **"Running the same script multiple times produces the same result."**
* If Apache is already installed, Ansible does nothing. It checks the *state* before acting.

### 4. What does `become: yes` mean?
It tells Ansible to use `sudo` (Run as Administrator/Root). This is required for installing software on Linux servers.