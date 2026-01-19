# API Interactions

## Tasks Overview
This folder contains custom scripts for interacting with REST APIs using both Python and cURL, satisfying criteria Ap3 through Ap6.

### Included Files
* **Ap3 - `Ap3_webex_custom.py`**: (Python) Authenticates with Webex API to create a specific room.
* **Ap4 - `Ap4_flask_form_api.py`**: (Python) A Flask micro-API that processes web form data and returns a JSON response.
* **Ap5 - `Ap5_restconf_get.sh`**: (cURL) Shell script performing a GET request against the IOS XE RESTCONF API.
* **Ap6 - `Ap6_restconf_post.sh`**: (cURL) Shell script simulating a form submission (POST) to configure a Loopback interface.

### Usage
1. **Python Scripts**:
   ```bash
   python3 Ap3_webex_custom.py
   python3 Ap4_flask_form_api.py