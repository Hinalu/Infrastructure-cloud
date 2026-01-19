#!/bin/bash
# Task Ap6: Custom REST-API experiment with curl (POST/Data)
# Creates a new Loopback interface via RESTCONF

echo "--- Executing RESTCONF POST Request ---"

curl -k -i -X "POST" \
  "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces" \
  -H 'Content-Type: application/yang-data+json' \
  -H 'Accept: application/yang-data+json' \
  -u 'cisco:cisco123!' \
  -d '{
    "ietf-interfaces:interface": {
      "name": "Loopback99",
      "description": "Created via Curl API Task Ap6",
      "type": "iana-if-type:softwareLoopback",
      "enabled": true,
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "10.99.99.1",
            "netmask": "255.255.255.0"
          }
        ]
      }
    }
  }'