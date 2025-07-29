from fpdf import FPDF
import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Project Report: Password Strength Analyzer & Wordlist Generator", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

# Initialize PDF
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", "", 12)

# Report content
content = f"""
Date: {datetime.date.today().strftime('%B %d, %Y')}
Developed by: Ayush

Introduction:
This project focuses on the development of a tool that helps users evaluate the strength of their passwords and generate customized wordlists using personal data. Such tools are crucial in cybersecurity to promote secure password practices and understand common vulnerabilities from weak password usage.

Abstract:
The Password Strength Analyzer uses the zxcvbn algorithm to evaluate how secure a given password is on a scale of 0 (weak) to 4 (strong). The tool also provides suggestions for improving password quality. Additionally, it features a Wordlist Generator that creates potential password combinations using personal information (name, pet name, year), which can be used in ethical hacking simulations and awareness training. The project supports both Command-Line Interface (CLI) and Graphical User Interface (GUI) using Tkinter.

Tools Used:
- Python 3.10+
- zxcvbn for password scoring and feedback
- argparse for command-line argument parsing
- Tkinter for graphical user interface
- itertools for generating wordlist permutations

Steps Involved in Building the Project:
1. Designed the overall architecture and modular folder structure.
2. Built the password_analyzer.py using zxcvbn for strength scoring.
3. Created wordlist_generator.py to generate combinations from user input.
4. Implemented CLI functionality in cli.py.
5. Developed GUI interface in gui.py using Tkinter.
6. Integrated both interfaces via a central main.py file.
7. Created test inputs, verified outputs, and made improvements.
8. Documented the entire project and prepared for GitHub deployment.

Conclusion:
Through this project, I learned to build and structure a modular Python application focused on cybersecurity. It enhanced my understanding of password evaluation mechanisms and demonstrated how attackers might construct wordlists using personal data. The dual interface support (CLI + GUI) improved the tool’s usability. Overall, the project reinforced secure password practices and provided valuable practical experience in ethical hacking and software development.

"""

# Clean content to avoid encoding issues
cleaned_content = "".join(c if ord(c) < 128 else '?' for c in content)

# Add content to PDF
for line in cleaned_content.strip().split("\n"):
    pdf.multi_cell(0, 10, line)

# Save the file
pdf.output("Password_Strength_Analyzer_Final_Report.pdf")
print("✅ PDF created successfully: Password_Strength_Analyzer_Final_Report.pdf")
