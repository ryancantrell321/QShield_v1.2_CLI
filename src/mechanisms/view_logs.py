import os
from src.mechanisms.logger import log_message


def open_logs():
    try:
        # Constructing the file path in the user's Documents folder
        documents_directory = os.path.expanduser("~/Documents")
        file_path = os.path.join(documents_directory, "qShield Event Logs", "events.log")

        # Open the file
        os.startfile(file_path)
        log_message("INFO", f"Opening file: {file_path}")

    except Exception as e:
        log_message("ERROR", f"Failed to open file: {e}")
        print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    open_logs()
