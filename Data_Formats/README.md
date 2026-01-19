# Data Formats & Models

## Tasks Overview
This folder demonstrates the ability to model network data in YAML and parse JSON data from various sources.

### Included Files
* **Js1 - `interfaces.yaml`**: A data model representing network interfaces in YAML format.
* **Js2 - `parse_webex.py`**: A Python script that filters a Webex API JSON response to extract Room Titles and IDs.
* **Js3 - `parse_network.py`**: A Python script that filters a DNA Center inventory JSON response to display Hostnames and IP addresses.
* **Js4 - `json_to_yaml.py`**: A utility script to convert JSON data into YAML format.
* **Yg1 - `yaml_to_json.py`**: A utility script to convert YAML data into JSON format.

### How to Run
```bash
python3 parse_webex.py
python3 parse_network.py