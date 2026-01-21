# API Interactions

## Tasks Overview
Custom scripts for interacting with REST APIs using Python and cURL (Criteria Ap3-Ap6).

### Included Files
* **Ap3 - `Ap3_webex_custom.py`**: Python script to create a Webex Room.
* **Ap4 - `Ap4_flask_form_api.py`**: Python Flask script simulating a Form API.
* **Ap5 - `Ap5_restconf_get.sh`**: cURL script to GET data from a router.
* **Ap6 - `Ap6_restconf_post.sh`**: cURL script to POST data (configure) a router.

---

## 🎓 Exam Prep: Concepts & Explanations

### 1. What is an API?
**API (Application Programming Interface)** is a set of rules allowing two software applications to talk to each other. We use **REST APIs**, which run over the web (HTTP).

### 2. HTTP Methods (Verbs)
* **GET:** Retrieve data (e.g., "Show me the interfaces").
* **POST:** Create new data (e.g., "Create a new room").
* **PUT:** Update/Replace data.
* **DELETE:** Remove data.

### 3. HTTP Status Codes
* **200 OK:** Success.
* **201 Created:** Success (specifically for creation, like POST).
* **400 Bad Request:** You sent invalid data.
* **401 Unauthorized:** You forgot your password/token.
* **404 Not Found:** The URL is wrong.

### 4. What is `requests`?
It is a popular Python library used to send HTTP requests.
* Code example: `response = requests.get(url, headers=headers)`
* **Headers:** Metadata sent with the request (like "Content-Type" or "Authorization").

### 5. What is cURL?
**cURL** (Client URL) is a command-line tool for transferring data.
* `-X`: Specifies the method (GET, POST).
* `-H`: Adds a header.
* `-d`: Adds data (the payload).
* `-k`: Skips SSL certificate verification (useful for labs).