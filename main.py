"""
Pandora QShield
Version: 1.2_CLI
Author: RyanCantrell321
Release: January 2025
Copyright: RyanCantrell321, Pandora Dynamics
License: GNU General Public License (GPL) v3.0
"""



import sys
from src.mechanisms.memory_cleaner import start_cleaner
from src.texts.texts import t4, t5, display
from src.mechanisms.text_wrap import justify_text, terminal_width
from src.mechanisms.logger import log_message
from src.mechanisms.view_logs import open_logs
from src.mechanisms.backup import backup
from src.mechanisms.restore import restore
from src.mechanisms.usage import usage, support
from colorama  import Fore, Style

log_message("INFO", "QShield is starting...")
start_cleaner()

while True:
    try:
        display()

        while True:
            print(t4)
            print()

            choice = int(input("Enter your choice (1-6): "))
            print()

            if choice == 1:
                log_message("INFO", "Backup mode selected")
                backup()
                continue

            elif choice == 2:
                log_message("INFO", "Restore mode selected")
                restore()
                continue

            elif choice == 3:
                log_message("INFO", "Opening Usage Guide")
                usage("usage.pdf")
                continue

            elif choice == 4:
                log_message("INFO", "Opening Logs")
                open_logs()
                continue

            elif choice == 5:
                support()
                continue

            elif choice == 6:
                log_message("INFO", "Exiting QShield")
                print("Exiting QShield...\n")
                sys.exit(0)

            else:
                log_message("WARNING", "Invalid choice")
                print(Fore.RED + justify_text(t5, terminal_width))
                print(Style.RESET_ALL)
                continue



    except Exception as e:
        log_message("ERROR", f"An error occurred: {e}")
        print(f"Error: {e}")
        continue

    else:
        break
