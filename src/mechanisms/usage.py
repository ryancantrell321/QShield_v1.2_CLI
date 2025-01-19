import webbrowser
import os
from src.mechanisms.logger import log_message
from src.mechanisms.any_key import any_key_to_continue


def usage(file_path):

    try:
        os.startfile(file_path)
        log_message("INFO", "Opening usage.pdf")
        any_key_to_continue()

    except Exception as e:
        log_message("ERROR", f"An error occurred: {e}")
        print(f"Error: {e}")

def support():
    print("To report bugs or issues or request a feature, please find contact details on GitHub"
          "")
    webbrowser.open("https://github.com/ryancantrell321/QShield_v1.2_CLI")
    log_message("INFO", "Opening GitHub")
    any_key_to_continue()