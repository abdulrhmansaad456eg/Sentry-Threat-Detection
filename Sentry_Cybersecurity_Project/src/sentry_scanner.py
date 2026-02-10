import tkinter as tk
from tkinter import filedialog, messagebox
import re
import os
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class SentryPro:
    def __init__(self, root):
        self.root = root
        self.root.title("SENTRY v2.0 - Threat Detection")
        self.root.geometry("750x550")
        self.root.configure(bg="#0d1117") # GitHub Dark Theme Background

        self.log_path = ""
        self.threats = []

        # --- UI STYLING ---
        title_lbl = tk.Label(root, text="SENTRY CYBER-ANALYZER", fg="#58a6ff", bg="#0d1117", font=("Courier", 20, "bold"))
        title_lbl.pack(pady=15)

        self.btn_select = tk.Button(root, text="LOAD LOG FILE", command=self.select_file, bg="#21262d", fg="white", relief="flat", padx=10)
        self.btn_select.pack()

        self.lbl_file = tk.Label(root, text="Awaiting Input...", fg="#8b949e", bg="#0d1117")
        self.lbl_file.pack(pady=5)

        # Result Terminal
        self.text_area = tk.Text(root, height=18, width=85, bg="#010409", fg="#39ff14", insertbackground="white", font=("Consolas", 10))
        self.text_area.pack(pady=10, padx=20)

        # Footer Buttons
        btn_frame = tk.Frame(root, bg="#0d1117")
        btn_frame.pack(pady=10)

        self.btn_scan = tk.Button(btn_frame, text="[ START SECURITY SCAN ]", state="disabled", bg="#238636", fg="white", font=("Arial", 10, "bold"), command=self.scan)
        self.btn_scan.pack(side="left", padx=10)

        self.btn_pdf = tk.Button(btn_frame, text="GENERATE PDF REPORT", state="disabled", bg="#1f6feb", fg="white", command=self.save_pdf)
        self.btn_pdf.pack(side="left", padx=10)

    def select_file(self):
        self.log_path = filedialog.askopenfilename()
        if self.log_path:
            self.lbl_file.config(text=f"LOADED: {os.path.basename(self.log_path)}")
            self.btn_scan.config(state="normal")

    def get_threat_info(self, type):
        info = {
            "Brute Force": "High risk of unauthorized system access via password guessing.",
            "SQL Injection": "Attempt to steal or corrupt the database via malicious queries.",
            "Path Traversal": "Attempt to access restricted system files (like /etc/passwd).",
            "Suspicious Script": "Execution of scripts in temporary directories, often indicating malware."
        }
        return info.get(type, "General suspicious activity detected.")

    def scan(self):
        self.threats = []
        # Patterns + Explanations
        patterns = {
            "Brute Force": r"Failed password",
            "SQL Injection": r"UNION SELECT|OR '1'='1'",
            "Path Traversal": r"\.\./\.\./",
            "Suspicious Script": r"\.sh|\.php\?|\.exe"
        }
        
        self.text_area.delete("1.0", "end")
        self.text_area.insert("end", f"[*] ANALYZING: {self.log_path}\n" + "="*70 + "\n")
        
        try:
            with open(self.log_path, 'r', errors='ignore') as f:
                for i, line in enumerate(f):
                    for name, pat in patterns.items():
                        if re.search(pat, line, re.I):
                            detail = self.get_threat_info(name)
                            entry = {
                                "line": i+1,
                                "type": name,
                                "content": line.strip()[:80],
                                "danger": detail
                            }
                            self.threats.append(entry)
                            self.text_area.insert("end", f"[!] {name} DETECTED AT LINE {i+1}\n")
                            self.text_area.insert("end", f"    INFO: {detail}\n\n")

            if not self.threats:
                self.text_area.insert("end", "[+] NO THREATS FOUND. SYSTEM SECURE.")
            else:
                self.btn_pdf.config(state="normal")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_pdf(self):
        path = filedialog.asksaveasfilename(defaultextension=".pdf")
        if not path: return
        
        c = canvas.Canvas(path, pagesize=letter)
        c.setTitle("Sentry Security Report")
        
        # Report Header
        c.setFont("Helvetica-Bold", 18)
        c.drawString(50, 750, "SENTRY SECURITY FORENSICS REPORT")
        c.setFont("Helvetica", 10)
        c.drawString(50, 735, f"Generated: {datetime.datetime.now()}")
        c.line(50, 730, 550, 730)

        y = 700
        for t in self.threats:
            if y < 100: c.showPage(); y = 750
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, y, f"THREAT: {t['type']} (Line {t['line']})")
            y -= 15
            c.setFont("Helvetica-Oblique", 10)
            c.drawString(60, y, f"Why it's dangerous: {t['danger']}")
            y -= 15
            c.setFont("Courier", 9)
            c.drawString(60, y, f"Log Evidence: {t['content']}")
            y -= 30
        
        c.save()
        messagebox.showinfo("Success", "Professional PDF Report Generated!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SentryPro(root)
    root.mainloop()