# Network Programmability (Netmiko, RESTCONF, NETCONF)

## Tasks Overview
This folder contains scripts for interacting with IOS XE devices using various programmability methods, satisfying criteria N1-N4.

### Included Files
* **N1 - `N1_netmiko_show.py`**: Uses the **Netmiko** library to SSH into a router and run `show ip interface brief`.
* **N2 - `N2_netmiko_config.py`**: Uses **Netmiko** to push configuration commands (creating Loopback101).
* **N3 - `N3_restconf_interface.py`**: Uses Python **Requests** to query the RESTCONF API for interface data (JSON).
* **N4 - `N4_netconf_edit.py`**: Uses **ncclient** to push an XML configuration payload via the NETCONF protocol (creating Loopback55).

### Usage
1. Ensure the router (192.168.56.101) is reachable and SSH/RESTCONF/NETCONF are enabled.
2. Run the scripts:
   ```bash
   python3 N1_netmiko_show.py
   python3 N2_netmiko_config.py
   python3 N3_restconf_interface.py
   python3 N4_netconf_edit.py