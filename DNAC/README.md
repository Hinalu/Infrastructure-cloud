# Cisco DNA Center Automation

## Tasks Overview
This folder contains the script for interacting with the Cisco DNA Center (DNAC) Sandbox, satisfying criterion Dna.

### Included Files
* **Dna - `Dna_sandbox.py`**: A Python script that:
    1. Authenticates with the Cisco DevNet Always-On Sandbox.
    2. Retrieves an authentication token (POST).
    3. Fetches the full network device inventory (GET).
    4. Filters and displays Hostname, Device Family, and Management IP.

### Usage
Run the script (ensure internet access is available):
```bash
python3 Dna_sandbox.py