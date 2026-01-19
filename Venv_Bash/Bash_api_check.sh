#!/bin/bash
# Task 7: Bash Script for API Availability Check
# Checks if the API is reachable before attempting to fetch data.

TARGET="https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
LOG_FILE="api_check.log"

echo "--- Starting API Check ---"

# 1. Check API Status (Silent mode, output only HTTP code)
# We use the DNAC auth endpoint as a test target
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" "$TARGET")

if [ "$STATUS" -eq 401 ] || [ "$STATUS" -eq 200 ]; then
    # 401 is actually a "Success" here because it means the server is reachable 
    # and asking for password (which we didn't provide in the check).
    echo "[$(date)] SUCCESS: API is reachable (Status: $STATUS)" | tee -a "$LOG_FILE"
    
    # 2. If reachable, we would run our python script
    echo "Triggering Python Script..."
    # python3 ../DNAC/Dna_sandbox.py
else
    echo "[$(date)] FAILURE: API Unreachable (Status: $STATUS)" | tee -a "$LOG_FILE"
fi