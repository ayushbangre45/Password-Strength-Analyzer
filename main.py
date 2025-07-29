import sys
from analyzer.cli import run_cli
from analyzer.gui import run_gui

if __name__ == "__main__":
    if "--cli" in sys.argv:
        run_cli()
    else:
        run_gui()
