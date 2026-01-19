from netmiko import ConnectHandler

# Task N1: Netmiko Show Command Experiment
# Connects to the router and retrieves the interface status

# Device details (Sandbox or Local Lab)
cisco_router = {
    'device_type': 'cisco_ios',
    'host':   '192.168.56.101',
    'username': 'cisco',
    'password': 'cisco123!',
    'port': 22,
}

def get_interface_status():
    print(f"Connecting to {cisco_router['host']}...")
    try:
        connection = ConnectHandler(**cisco_router)
        print("Success! Sending command: show ip interface brief")
        
        output = connection.send_command("show ip interface brief")
        print("\n--- Command Output ---")
        print(output)
        
        connection.disconnect()
    except Exception as e:
        print(f"Connection Failed: {e}")

if __name__ == "__main__":
    get_interface_status()