# Data Formats & Models

## Tasks Overview
This folder demonstrates parsing JSON/YAML and data model conversion (Criteria Js1-Js4, Yg1).

### Included Files
* **Js1 - `interfaces.yaml`**: Network data modeled in YAML.
* **Js2 - `parse_webex.py`**: Filters a Webex JSON API response.
* **Js3 - `parse_network.py`**: Filters a DNA Center JSON response.
* **Js4 - `json_to_yaml.py`**: Converts JSON objects to YAML format.
* **Yg1 - `yaml_to_json.py`**: Converts YAML text to JSON objects.

---

## 🎓 Exam Prep: Concepts & Explanations

### 1. What is Parsing?
**Parsing** is the process of analyzing a string of symbols (like text in a file) and converting it into a data structure that the computer can understand and manipulate.
* **Serialization:** Converting Python objects (dicts/lists) -> Text (JSON/YAML string).
* **Deserialization:** Converting Text (JSON/YAML string) -> Python objects.

### 2. JSON vs. YAML
* **JSON (JavaScript Object Notation):** Uses curly braces `{}` and brackets `[]`. It is strict and commonly used for APIs (web data).
* **YAML (YAML Ain't Markup Language):** Uses indentation (spaces) and dashes `-`. It is human-readable and commonly used for Configuration files (Ansible, Docker).

### 3. Key Python Functions Used
* `import json`: Loads the Python library to handle JSON.
* `json.loads(string)`: "Load String". Converts a JSON text string into a Python Dictionary.
* `json.dumps(object)`: "Dump String". Converts a Python Dictionary into a JSON text string.
* `yaml.safe_load(file)`: Safely reads a YAML file and converts it to Python.

### 4. Lists vs. Dictionaries
* **List (`[]`):** An ordered collection of items. Accessed by index (e.g., `items[0]`).
* **Dictionary (`{}`):** A collection of Key-Value pairs. Accessed by key (e.g., `device['hostname']`).