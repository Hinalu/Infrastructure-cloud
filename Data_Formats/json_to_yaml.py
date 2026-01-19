# Task Js4: Convert JSON to YAML
import json
import yaml

# Sample JSON Data (Inline)
json_data = {
    "device": {
        "hostname": "CSR1000v",
        "role": "router",
        "interfaces": ["Gi1", "Gi2", "Lo0"]
    }
}

def convert_json_to_yaml():
    # Convert dictionary to YAML string
    yaml_output = yaml.dump(json_data, sort_keys=False)
    print("--- JSON to YAML Output ---")
    print(yaml_output)
    
    # Optional: Save to file
    with open('output.yaml', 'w') as file:
        yaml.dump(json_data, file)

if __name__ == "__main__":
    convert_json_to_yaml()