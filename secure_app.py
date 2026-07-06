import os
import re
import subprocess
from dotenv import load_dotenv

# Load safe environment variables from an external configuration file
load_dotenv()

# 1. SAFE SECRETS HANDLING
DB_PASSWORD = os.getenv("DB_PASSWORD", "FallbackSafeLocalPass")
API_KEY = os.getenv("API_KEY", "FallbackSafeLocalKey")

def secure_login(username):
    # 2. SQL INJECTION DEFENSE (Parameterized Queries Simulation)
    query = "SELECT * FROM users WHERE username = ?"
    print(f"[DEBUG] Executing Secure Query: {query}")
    print(f"with value: ({username})")
    return [] 

def secure_ping(host_input):
    # 3. OS COMMAND INJECTION DEFENSE
    # Regular Expression Validation for standard IPv4 addresses
    ip_pattern = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"
    
    if not re.match(ip_pattern, host_input.strip()):
        return "[ERROR] Validation Failed: Input must be a valid IPv4 address."
    
    # Safe Subprocess Execution (shell=False)
    print(f"[DEBUG] Executing Safe Subprocess List: ['ping', '-c', '1', '{host_input.strip()}']")
    try:
        result = subprocess.run(
            ["ping", "-c", "1", host_input.strip()],
            shell=False,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout
    except Exception as e:
        return f"[ERROR] Execution failed: {str(e)}"

if __name__ == "__main__":
    print("--- SECURE CODE LAB STARTING ---")
    
    print("\n[!] Testing SQLi payload against secure application: alice' OR '1'='1")
    print(f'Result (Empty or Safe): {secure_login("alice\' OR \'1\'=\'1")}')
    
    print("\n[!] Testing Command Injection payload against secure application: 127.0.0.1 && echo 'HACKED SYSTEM'")
    print(f'Result: {secure_ping("127.0.0.1 && echo \'HACKED SYSTEM\'")}')
    
    print("\n[!] Testing valid IP input: 127.0.0.1")
    print(f'Result: {secure_ping("127.0.0.1")}')