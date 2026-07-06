import os

# 1. HARDCODED SECRETS (Vulnerability)
# Real production keys should never be exposed in plaintext source code
DB_PASSWORD = "SuperSecretAdminPassword123!"
API_KEY = "ca_live_98765abcde"

def vulnerable_login(username):
    # 2. SQL INJECTION (Vulnerability)
    # Direct string formatting allows attackers to rewrite query logic
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print(f"[DEBUG] Executing Vulnerable Query: {query}")
    
    # Simulating database evaluation
    if "OR '1'='1" in username:
        return [("1", "admin", DB_PASSWORD)]
    return []

def vulnerable_ping(host_input):
    # 3. OS COMMAND INJECTION (Vulnerability)
    # Passing raw user input directly to a system shell execution call
    print(f"[DEBUG] Executing Vulnerable Shell Command: ping -c 1 {host_input}")
    
    # os.popen executes directly via the system shell
    output = os.popen(f"ping -c 1 {host_input}").read()
    return output

if __name__ == "__main__":
    print("--- VULNERABLE CODE LAB STARTING ---")
    
    # Test SQLi
    print("\n[!] Testing SQLi payload against vulnerable application:")
    sqli_payload = "alice' OR '1'='1"
    print(f"Result: {vulnerable_login(sqli_payload)}")
    
    # Test Command Injection
    print("\n[!] Testing Command Injection payload against vulnerable application:")
    cmd_payload = "127.0.0.1 && echo 'HACKED SYSTEM'"
    print(f"Result:\n{vulnerable_ping(cmd_payload)}")