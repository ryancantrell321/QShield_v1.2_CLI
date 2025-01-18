import os
import shutil
import zipfile
from src.mechanisms.logger import log_message
from colorama import init, Fore, Style
from datetime import datetime as dt
from src.mechanisms.progress_bar import display_progress_bar
from src.mechanisms.any_key import any_key_to_continue


def backup():

    try:
        print("Selected folder to backup: %localappdata%/qBittorrent")
        print("Selected folder to backup: %appdata%/qBittorrent")
        print()
        save_path = input("Enter the path to save the backup file: ")

        init(autoreset=True)

        def backup_data(backup_location, backup_date):
            try:

                localappdata_path = os.path.join(os.getenv("LOCALAPPDATA"), "qBittorrent")
                appdata_path = os.path.join(os.getenv("APPDATA"), "qBittorrent")

                backup_dir = os.path.join(backup_location, f"QShield_Qbt_Backup_{backup_date}")
                os.makedirs(backup_dir, exist_ok=True)

                localappdata_backup = os.path.join(backup_dir, "localappdata")
                appdata_backup = os.path.join(backup_dir, "appdata")

                shutil.copytree(localappdata_path, localappdata_backup)
                shutil.copytree(appdata_path, appdata_backup)

                zip_path = os.path.join(backup_location, f"QShield_Qbt_Backup_{backup_date}.zip")
                with zipfile.ZipFile(zip_path, "w") as backup_zip:
                    files = []
                    for folder_name, subfolders, filenames in os.walk(backup_dir):
                        for filename in filenames:
                            files.append(os.path.join(folder_name, filename))

                    total_files = len(files)

                    for index, file_path in enumerate(files, start=1):
                        backup_zip.write(file_path, os.path.relpath(file_path, backup_dir))
                        display_progress_bar(index, total_files)

                print()

                shutil.rmtree(backup_dir)
                print(Fore.GREEN + f"Backup completed successfully: {zip_path}")
                any_key_to_continue()
                print()
                log_message("INFO", f"Backup completed successfully: {zip_path}")

            except Exception as err:
                print(Fore.RED + f"Failed to backup data: {err}")
                any_key_to_continue()
                print()
                log_message("ERROR", f"Failed to backup data: {err}")
                raise

        if not os.path.exists(save_path):
            print(Fore.RED + "The specified directory does not exist. Please try again.")
            any_key_to_continue()
            print()
            return

        b_date = dt.now().strftime("%Y%m%d_%H%M%S")
        backup_data(save_path, b_date)

    except Exception as e:
        log_message("ERROR", f"An error occurred: {e}")
        print(f"Error: {e}")
