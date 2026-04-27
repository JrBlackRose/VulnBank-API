# 🏦 VulnBank-API

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-green.svg)
![Docker](https://img.shields.io/badge/Container-Docker-blue.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)

**VulnBank-API** is an intentionally vulnerable REST API built with Python/Flask. It is designed as a local sandbox for offensive security testing, specifically focusing on exploiting Authentication Bypass via SQL Injection (SQLi) and Remote Code Execution (RCE) via OS Command Injection.

> ⚠️ **Disclaimer:** This application is strictly for educational purposes and authorized vulnerability research. Do not deploy this on a public-facing server.

## 🚀 Quick Start (One-Click Setup)

1. Clone the repository:
   ```bash
   git clone [https://github.com/jrblackrose/VulnBank-API.git](https://github.com/jrblackrose/VulnBank-API.git)
   cd VulnBank-API
2. Spin up the vulnerable environment:
   ```bash
   docker-compose up --build -d
   ```
   The API will be live at http://localhost:5000.

3. 🎯 Vulnerability Scope
 -  SQL Injection (SQLi) - Authentication Bypass
Endpoint: POST /api/v1/login

Description: The login endpoint concatenates user input directly into the SQLite query string without parameterization.

Goal: Bypass authentication and extract the admin role.

 -  OS Command Injection (RCE)
Endpoint: POST /api/v1/system/ping

Description: A network diagnostic tool that takes an IP address and passes it directly to the system's ping utility using os.popen().

Goal: Chain shell commands to achieve remote code execution on the container.

4. 💥 Running the Exploits
A custom Python Proof of Concept (PoC) is provided in the /exploits directory to demonstrate the RCE vulnerability.
```bash
cd exploits
pip install requests

# Execute standard system commands
python3 poc_rce.py -t http://localhost:5000/api/v1/system/ping -c "whoami"
python3 poc_rce.py -t http://localhost:5000/api/v1/system/ping -c "cat /etc/passwd"
```
📜 License
Distributed under the MIT License. See LICENSE for more information.

Developed by jrblackrose. Think in Code.
### 5. `LICENSE`
```text
MIT License

Copyright (c) 2026 jrblackrose

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
