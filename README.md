🛡️ SENTRY v2.0
Advanced Log Analysis & Threat Detection

Sentry is a standalone defensive cybersecurity tool that performs automated log analysis, threat detection, and forensic reporting.

It parses raw system and server logs to uncover sophisticated attack patterns, classifies threats by severity, and generates professional forensic reports suitable for audits, incident response, and security investigations.

Built with a privacy first and offline first philosophy, Sentry runs entirely on the local machine with zero external dependencies or telemetry.

🚀 Key Features
🔍 Heuristic Detection Engine

Detects common and high impact attacks using advanced Regex pattern matching:

SQL Injection (SQLi)

SSH Brute Force attempts

Path Traversal exploits

🧠 Contextual Intelligence

Each alert includes:

Risk level

Clear explanation of the threat

Why it is dangerous

Raw evidence lines from logs

🌙 Dark Theme UI

Custom styled Cyber Analyzer interface designed for:

High visibility

Long monitoring sessions

Reduced eye strain

📄 Forensic PDF Reporting

Generate timestamped, tamper evident reports that include:

Threat summaries

Severity classification

Raw log evidence

Chain of custody friendly format

⚡ Lightweight Architecture

Standalone executable

No installation required

No Python environment needed

< 20MB compressed build

Works offline

🧰 Technical Stack
Component	Technology
Language	Python 3.10+
GUI	Tkinter (Custom Dark Mode)
Detection	Regular Expressions (Regex)
PDF Engine	ReportLab
Packaging	PyInstaller
Compression	UPX
🧩 Use Cases

Sentry is designed for practical defensive security scenarios:

Blue Team log triage

Incident response investigations

SOC training labs

Student cybersecurity exercises

Offline forensic audits

Small business security monitoring

🎯 Design Goals

Sentry was built with the following principles:

Fast offline analysis without internet dependency

Privacy first with zero telemetry or data collection

Transparent and explainable detections

Lightweight and portable for field use

Simple enough for students, powerful enough for professionals

🔐 Privacy & Security

Sentry respects user privacy by design:

Fully offline operation

No cloud services

No telemetry

No external API calls

Logs never leave the local machine

All analysis happens locally.

⚠️ Limitations

To remain lightweight and portable, Sentry currently has some constraints:

Regex based detection may miss heavily obfuscated payloads

Not a replacement for full SIEM or enterprise SOC platforms

Designed primarily for small to medium log files (<500MB recommended)

Batch analysis only (no real time monitoring yet)

These tradeoffs keep the tool fast and dependency free.

🗺️ Roadmap

Planned improvements for future versions:

Real time log streaming mode

Additional detections (XSS, RCE, malware signatures)

Risk score dashboard

JSON and CSV export

YARA rule support

Plugin based detection engine

Multi log correlation
