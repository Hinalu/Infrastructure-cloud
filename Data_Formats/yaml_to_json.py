# Task Yg1: Convert YAML to JSON
import json
import yaml

# Sample YAML Data (Inline)
yaml_data = """
device:
  hostname: Switch-Core
  role: switch
  vlan:
    - id: 10
      name: Data
    - id: 20
      name: Voice
"""

def convert_yaml_to_json():
    # Parse YAML string into Python dictionary
    python_dict = yaml.safe_load(yaml_data)
    
    # Convert dictionary to JSON string
    json_output = json.dumps(python_dict, indent=4)
    print("--- YAML to JSON Output ---")
    print(json_output)

if __name__ == "__main__":
    convert_yaml_to_json()