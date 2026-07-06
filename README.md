# Secure Coding Review Lab 🛡️💻

## Project Overview
[cite_start]This project serves as an interactive source code audit lab designed to demonstrate common application security vulnerabilities and their corresponding secure remediation strategies[cite: 10]. [cite_start]It contrasts an intentionally insecure implementation (`vulnerable_app.py`) against a hardened, defensive implementation (`secure_app.py`) across three classic security flaws: SQL Injection (SQLi), OS Command Injection, and Hardcoded Secrets[cite: 10].

[cite_start]By moving from flawed design patterns to modern defensive coding architectures, this laboratory environment showcases foundational principles of the Secure Software Development Life Cycle (SSDLC) and Application Security (AppSec)[cite: 11, 27, 29].

---

## Technical Architecture & Core Vulnerabilities

### 1. SQL Injection (SQLi)
* **The Flaw (`vulnerable_app.py`):** Utilizes direct string interpolation/concatenation to embed user input parameters straight into the dynamic SQL query string execution path. This permits malicious users to append SQL operators (e.g., `' OR '1'='1`) to manipulate database logical execution flows.
* **The Remediation (`secure_app.py`):** Implements **Parameterized Queries (Prepared Statements)** via the standard database interface handler. Parameterization cleanly decouples the processing instructions (the query code) from user inputs (the data state), nullifying input manipulation vectors.

### 2. OS Command Injection
* **The Flaw (`vulnerable_app.py`):** Directly feeds unvalidated text commands through native system shell subprocess invocation routes (`shell=True`). Attackers can append shell control operators (like `;`, `&&`, or `|`) to execute unauthorized operational commands.
* **The Remediation (`secure_app.py`):** Employs strict **Regex Validation** to enforce proper string structure (e.g., matching exact IPv4 boundaries), while invoking execution using array-based argument tokens with shell compilation disabled (`shell=False`). 

### 3. Hardcoded Secrets (Credential Leaks)
* **The Flaw (`vulnerable_app.py`):** Stores cryptographic authentication secrets and sensitive application service keys directly inside the source code file as plain text variables, presenting an instant data breach risk if public repository tracking occurs.
* **The Remediation (`secure_app.py`):** Implements externalized environment isolation using `python-dotenv`. Production secrets are offloaded to an explicit `.env` file, reading the keys safely into volatile operational runtime memory utilizing `os.getenv()`.

---

## Laboratory Setup & Prerequisites

### Installation
Ensure you have Python 3 installed on your local host system environment. Install the operational dependencies via your command line shell interpreter interface:

```bash
pip install python-dotenv

python vulnerable_app.py
python secure_app.py
