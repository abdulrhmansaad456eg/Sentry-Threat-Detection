# 🛡️ SENTRY v2.0
### **Advanced Log Analysis & Threat Detection**

Sentry is a standalone, **privacy-first** defensive cybersecurity tool designed for automated log analysis, threat detection, and forensic reporting. It parses raw system logs to uncover sophisticated attack patterns, classifies threats by severity, and generates professional forensic reports suitable for audits and incident response.



---

## 🚀 Key Features

### 🔍 Heuristic Detection Engine
Detects common and high-impact attacks using advanced Regex pattern matching:
* **SQL Injection (SQLi):** Malicious database query attempts.
* **SSH Brute Force:** Repeated unauthorized access attempts.
* **Path Traversal:** Directory climbing and sensitive file access.

### 🧠 Contextual Intelligence
Each alert is enriched with actionable data:
* **Risk Level:** Categorized from Low to Critical.
* **Threat Explanation:** Why the pattern is dangerous.
* **Raw Evidence:** Direct log lines for immediate validation.

### 📄 Forensic PDF Reporting
Generate timestamped, tamper-evident reports including:
* Threat summaries and severity classification.
* Raw log evidence for chain-of-custody documentation.

### ⚡ Lightweight Architecture
* **Standalone:** Single executable under 20MB.
* **Portable:** No installation or Python environment needed.
* **Offline:** Zero external dependencies or telemetry.

---

## 🛠️ Technical Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.10+ |
| **GUI** | Tkinter (Custom Dark Mode) |
| **Detection Engine** | Regular Expressions (Regex) |
| **PDF Engine** | ReportLab |
| **Packaging** | PyInstaller & UPX |

---

## 🧩 Use Cases

* **Blue Team Triage:** Quickly filter noise during security incidents.
* **Incident Response:** Generate audit-ready reports for stakeholders.
* **SOC Training:** Ideal for cybersecurity students and lab exercises.
* **Offline Audits:** Secure analysis for air-gapped systems.

---

## 🎯 Design Principles

> **Privacy First:** Fully offline operation. Logs never leave the local machine.  
> **Transparency:** Detections are explainable and visible to the analyst.  
> **Efficiency:** Designed for high visibility during long monitoring sessions via a Dark Theme UI.

---

## ⚠️ Limitations & Roadmap

### Current Constraints
* Regex-based detection may miss heavily obfuscated payloads.
* Optimized for batch analysis (no real-time streaming yet).
* Recommended for log files under 500MB.

### Roadmap 🗺️
- [ ] Real-time log streaming mode.
- [ ] Additional detections (XSS, RCE, Malware signatures).
- [ ] Risk score dashboard and visualization.
- [ ] JSON and CSV export support.
- [ ] YARA rule integration.

---

## 🔐 Privacy & Security
Sentry respects user privacy by design. There are no cloud services, no external API calls, and zero data collection. All analysis happens strictly on the host machine.

---

## 💻 Getting Started
1. **Download** the latest `Sentry.exe` from the Releases page.
2. **Run** the application (no admin rights required).
3. **Upload** your `.log` or `.txt` file.
4. **Analyze** and export your Forensic PDF Report.

---

*Developed for the security community with a focus on privacy and portability.*
