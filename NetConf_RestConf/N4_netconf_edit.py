from ncclient import manager

# Task N4: NETCONF Experiment
# Uses NETCONF (XML) to configure a Loopback interface

router = {
    'host': '192.168.56.101',
    'port': 830,
    'username': 'cisco',
    'password': 'cisco123!',
    'hostkey_verify': False
}

# XML Payload for creating Loopback 55
netconf_config = """
<config>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback55</name>
      <description>Configured via NETCONF Task N4</description>
      <type xmlns:iana="urn:ietf:params:xml:ns:yang:iana-if-type">iana:softwareLoopback</type>
      <enabled>true</enabled>
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>10.55.55.1</ip>
          <netmask>255.255.255.0</netmask>
        </address>
      </ipv4>
    </interface>
  </interfaces>
</config>
"""

def edit_config_netconf():
    print(f"Connecting to {router['host']} via NETCONF port 830...")
    with manager.connect(**router) as m:
        print("Sending Edit-Config RPC...")
        response = m.edit_config(target='running', config=netconf_config)
        print("Response from Router:")
        print(response)

if __name__ == "__main__":
    edit_config_netconf()