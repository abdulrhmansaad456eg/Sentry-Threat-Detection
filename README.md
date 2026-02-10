# 🛡️ SENTRY v2.0 | Advanced Log Analysis & Threat Detection

**Sentry** is a standalone cybersecurity tool designed to provide automated security monitoring and forensic reporting. It parses raw system logs to detect sophisticated attack patterns, classifies threats by risk level, and generates professional forensic reports for security audits.

---

## 🚀 Key Features

* **Heuristic Detection Engine:** Identifies SQL Injection (SQLi), SSH Brute-Force, and Path Traversal attacks using advanced Regex pattern matching.
* **Contextual Intelligence:** Provides detailed explanations for each detected threat, explaining *why* it is dangerous to the system.
* **Dark-Theme UI:** Optimized "Cyber-Analyzer" interface built for high-visibility monitoring.
* **Forensic PDF Generation:** Exports timestamped, tamper-evident security reports including raw evidence lines for chain-of-custody.
* **Lightweight Architecture:** Zero-dependency standalone executable (<20MB) requiring no installation or Python environment.

---

## 📸 Screenshots

> **Note to Reviewers:** The images below demonstrate the tool in action against a simulated compromised server log.

| Security Dashboard | Forensic PDF Report |
| :--- | :--- |
| ![Interface](screenshots/interface.png) | ![PDF Report](screenshots/pdf_report.png) |

---

## 🛠️ Technical Stack

* **Language:** Python 3.10+
* **GUI:** Tkinter (Custom Styled Dark Mode)
* **PDF Engine:** ReportLab
* **Analysis:** Regular Expressions (Regex)
* **Build Tool:** PyInstaller with UPX compression

---

## 🧪 Testing Instructions (For GKS Reviewers)

You can test the tool's detection capabilities in under 60 seconds:

1.  **Download:** Navigate to the `dist/` folder and download `sentry_scanner.exe` (or the `.zip` version).
2.  **Launch:** Run the executable on a Windows machine (no installation required).
3.  **Load Logs:** Click **"LOAD LOG FILE"** and select the provided sample file: `tests/compromised_log.txt`.
4.  **Analyze:** Click **"START SECURITY SCAN"**. The terminal will highlight detected threats in green.
5.  **Audit:** Click **"GENERATE PDF REPORT"** to see the professional forensic output.

---

## 📂 Project Structure

```text
Sentry-Threat-Detection/
├── src/
│   └── sentry_scanner.py       # Main Source Code (Professor Review)
├── dist/
│   └── sentry_scanner.exe      # Compiled Windows Executable
├── tests/
│   └── compromised_log.txt     # Sample data for testing
├── screenshots/                # Documentation images
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
