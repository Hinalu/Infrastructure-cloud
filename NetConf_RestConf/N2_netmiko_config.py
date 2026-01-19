from netmiko import ConnectHandler

# Task N2: Netmiko Config Experiment
# Connects to the router and configures a Loopback interface

cisco_router = {
    'device_type': 'cisco_ios',
    'host':   '192.168.56.101',
    'username': 'cisco',
    'password': 'cisco123!',
}

config_commands = [
    'interface Loopback101',
    'description Configured via Netmiko Task N2',
    'ip address 10.101.101.1 255.255.255.0',
    'no shutdown'
]

def configure_router():
    print(f"Connecting to {cisco_router['host']} for configuration...")
    try:
        connection = ConnectHandler(**cisco_router)
        print("Sending configuration commands...")
        
        output = connection.send_config_set(config_commands)
        print("\n--- Configuration Output ---")
        print(output)
        
        # Verify the change
        check = connection.send_command("show ip int brief | include Loopback101")
        print("\n--- Verification ---")
        print(check)
        
        connection.disconnect()
    except Exception as e:
        print(f"Configuration Failed: {e}")

if __name__ == "__main__":
    configure_router()