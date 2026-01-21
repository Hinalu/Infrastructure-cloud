# Cisco DNA Center Automation

## Tasks Overview
Script for interacting with the Cisco DNA Center Sandbox (Criterion Dna).

### Included Files
* **Dna - `Dna_sandbox.py`**: Authenticates and fetches device inventory.

---

## 🎓 Exam Prep: Concepts & Explanations

### 1. What is SDN?
**SDN (Software Defined Networking)** separates the Control Plane (Brain) from the Data Plane (Muscle).
* **DNA Center:** Is the "Controller" for Cisco Enterprise networks. It manages all switches and routers centrally.

### 2. Authentication Flow (Token)
APIs are stateless. They don't remember you between clicks.
1. We send a **Username/Password** (Basic Auth) to the `/token` endpoint.
2. The server gives us a specific **Token** string (like a temporary badge).
3. For all future requests, we put that Token in the `X-Auth-Token` header.

### 3. Why `verify=False`?
In Python `requests`, this parameter disables SSL Certificate verification. We do this in labs because the Sandbox often uses a "Self-Signed Certificate" which browsers/Python don't trust by default. In production, this should be `True`.