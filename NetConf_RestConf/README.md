# Network Programmability

## Tasks Overview
Scripts for interacting with IOS XE using Netmiko, RESTCONF, and NETCONF (Criteria N1-N4).

### Included Files
* **N1 - `N1_netmiko_show.py`**: SSH connection to run CLI commands.
* **N2 - `N2_netmiko_config.py`**: SSH connection to send config commands.
* **N3 - `N3_restconf_interface.py`**: REST API call to get interface data.
* **N4 - `N4_netconf_edit.py`**: NETCONF RPC to edit configuration.

---

## 🎓 Exam Prep: Concepts & Explanations

### 1. SSH vs. NETCONF vs. RESTCONF
* **SSH (Netmiko):** Screen scraping. It mimics a human typing CLI commands. Good for legacy devices.
* **NETCONF:** Uses SSH but sends **XML** data. It is transactional (atomic) and standardized.
* **RESTCONF:** Uses HTTP (HTTPS) and typically sends **JSON** (or XML). Easier for web developers to use.

### 2. What is YANG?
**YANG** is a data modeling language. It defines the *structure* of the data.
* Think of YANG as the "Blueprint" or "Template".
* Think of XML/JSON as the actual "House" built from that blueprint.

### 3. Libraries Used
* **Netmiko:** Python library to simplify SSH connections to network devices.
* **ncclient:** Python library specifically for acting as a NETCONF client.

### 4. What is a "Namespace" (xmlns)?
In the NETCONF XML (`N4_netconf_edit.py`), you see `xmlns="..."`. This is a **Namespace**. It ensures that "interface" means "Cisco IOS Interface" and not "User Interface". It prevents naming conflicts.