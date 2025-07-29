Password Strength Analyzer & Wordlist Generator

This project is a Python-based tool that helps users:
1. Analyze the strength of a given password.
2. Generate a custom wordlist using personal data (name, pet, year).

The tool supports both Command Line Interface (CLI) and Graphical User Interface (GUI) modes.

Features

- Password strength scoring using the `zxcvbn` algorithm  
- CLI support with `argparse`  
- GUI using `Tkinter`  
- Custom wordlist generator using name, pet, and year  
- Modular and easy-to-understand codebase  

Technologies Used

- Python 3.10+  
- zxcvbn  
- argparse  
- tkinter  
- itertools  

Installation

Install required dependencies:
pip install zxcvbn nltk

Usage
Run GUI Mode
python main.py

Run CLI Mode
python main.py --cli --password Password@2025 --name John --pet Bruno --year 2024

This will:

Score the password
Provide suggestions
Generate a custom wordlist and save it to wordlists/custom_wordlist.txt

Contribution
Pull requests are welcome! Please open an issue first to discuss what you would like to change.

Developed by
Ayush Bangre
Cyber Security Engineering Student
