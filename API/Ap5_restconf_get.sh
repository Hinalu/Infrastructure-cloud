#!/bin/bash
# Task Ap5: Custom REST-API experiment with curl (GET)
# Retrieves interface information from the CSR1000v router

echo "--- Executing RESTCONF GET Request ---"

curl -k -i -X "GET" \
  "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces" \
  -H 'Accept: application/yang-data+json' \
  -u 'cisco:cisco123!'