import argparse
from analyzer.password_analyzer import analyze_password
from analyzer.wordlist_generator import generate_wordlist

def run_cli():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer & Wordlist Generator")
    parser.add_argument("--password", help="Password to analyze")
    parser.add_argument("--name", help="Name for wordlist")
    parser.add_argument("--pet", help="Pet name for wordlist")
    parser.add_argument("--year", help="Year for wordlist")

    args = parser.parse_args()

    if args.password:
        result = analyze_password(args.password)
        print(f"Score: {result['score']}/4")
        print("Feedback:", result['feedback'])

    if args.name and args.pet and args.year:
        path = generate_wordlist(args.name, args.pet, args.year)
        print(f"Wordlist saved to {path}")
