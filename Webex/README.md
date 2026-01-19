# Webex Automation

## Tasks Overview
This folder contains scripts to automate Webex Teams interactions, satisfying criteria W1 and W2.

### Included Files
* **W2 - `W2_manage_spaces.py`**: A complete lifecycle script that:
    1. **Creates** a new Webex space named "DevNet Skills Exam Room".
    2. **Posts** a message into that room (satisfying Skills Exam Task 6).
    3. **Deletes** the room after a short delay to clean up.

### Usage
1. Open `W2_manage_spaces.py` and replace `YOUR_ACCESS_TOKEN_HERE` with your actual Webex Bot or Personal Token.
2. Run the script:
   ```bash
   python3 W2_manage_spaces.py