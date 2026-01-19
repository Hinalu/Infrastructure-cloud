# Ansible Automation

## Tasks Overview
This folder contains Ansible playbooks for configuring both network devices (IOS XE) and servers (Linux), satisfying criteria An1-An3 and As1-As3.

### Included Files
* **`ansible.cfg`**: Configuration file to disable host key checking and set defaults.
* **`hosts`**: Inventory file defining the `routers` and `webservers` groups.
* **An2 - `An2_ios_facts.yml`**: Connects to a CSR1000v router to gather facts and configure the logging buffer size to 5000.
* **As2 - `As2_apache_install.yml`**: Connects to a Linux server to install Apache2, enable modules, and deploy a custom HTML landing page.

### Usage
Run the playbooks using the `ansible-playbook` command:
```bash
# Run the Network Playbook
ansible-playbook An2_ios_facts.yml

# Run the Server Playbook
ansible-playbook As2_apache_install.yml