from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# --- Database Setup (Executes on startup) ---
def init_db():
    conn = sqlite3.connect('vulnbank.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)''')
    c.execute("INSERT OR IGNORE INTO users (id, username, password, role) VALUES (1, 'admin', 'SuperSecretAdminPassword123!', 'admin')")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return jsonify({"status": "online", "message": "Welcome to the VulnBank API V1.0"}), 200

# [VULNERABILITY 1: SQL Injection]
@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing credentials"}), 400

    username = data['username']
    password = data['password']

    conn = sqlite3.connect('vulnbank.db')
    c = conn.cursor()
    
    # FATAL FLAW: Direct string concatenation allows SQLi
    query = f"SELECT role FROM users WHERE username = '{username}' AND password = '{password}'"
    
    try:
        c.execute(query)
        result = c.fetchone()
        
        if result:
            return jsonify({"status": "success", "role": result[0], "message": "Authentication successful."}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid credentials."}), 401
    except sqlite3.Error as e:
        # Verbose error handling leaks database information
        return jsonify({"status": "error", "message": f"Database error: {e}"}), 500
    finally:
        conn.close()

# [VULNERABILITY 2: Remote Code Execution (OS Command Injection)]
@app.route('/api/v1/system/ping', methods=['POST'])
def ping_server():
    data = request.json
    if not data or 'ip' not in data:
        return jsonify({"error": "Missing IP address parameter"}), 400

    target_ip = data['ip']
    
    # FATAL FLAW: No input sanitization before passing to the OS shell
    command = f"ping -c 3 {target_ip}"
    
    try:
        # Executing system command directly
        output = os.popen(command).read()
        return jsonify({"status": "success", "output": output}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Running on 0.0.0.0 to allow external access within the Docker network
    app.run(host='0.0.0.0', port=5000, debug=False)
