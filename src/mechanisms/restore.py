import os
import shutil
import zipfile
from src.mechanisms.logger import log_message
from colorama import init, Fore
from src.mechanisms.progress_bar import display_progress_bar
from src.mechanisms.any_key import any_key_to_continue

def restore():

    try:
        print("Restore Mode Selected!")
        print("Source folders to restore to: %localappdata%/qBittorrent and %appdata%/qBittorrent")
        print()

        rf = input("Enter the path to the backup file to restore: ").strip()

        init(autoreset=True)

        if not os.path.exists(rf):
            print(Fore.RED + "The specified backup file does not exist. Please try again.")
            any_key_to_continue()
            print()
            return

        def restore_data(restore_file):
            try:
                # Validate the restore file
                if not os.path.basename(restore_file).startswith("QShield_Qbt_Backup"):
                    print(Fore.RED + "Error: Selected file is not a valid QShield backup file.")
                    log_message("ERROR", "Attempted restore with an invalid file.")
                    return


                temp_restore_dir = os.path.join(os.getenv("LOCALAPPDATA"), "Temp", "QShield_Restore")

                if os.path.exists(temp_restore_dir):
                    shutil.rmtree(temp_restore_dir)

                os.makedirs(temp_restore_dir, exist_ok=True)

                with zipfile.ZipFile(restore_file, "r") as zip_ref:
                    files = zip_ref.namelist()
                    total_files = len(files)

                    for index, file in enumerate(files, start=1):
                        zip_ref.extract(file, temp_restore_dir)
                        display_progress_bar(index, total_files)

                print()


                localappdata_restore = os.path.join(temp_restore_dir, "localappdata")
                appdata_restore = os.path.join(temp_restore_dir, "appdata")

                if os.path.exists(localappdata_restore):
                    shutil.copytree(localappdata_restore, os.path.join(os.getenv("LOCALAPPDATA"), "qBittorrent"), dirs_exist_ok=True)

                if os.path.exists(appdata_restore):
                    shutil.copytree(appdata_restore, os.path.join(os.getenv("APPDATA"), "qBittorrent"), dirs_exist_ok=True)


                shutil.rmtree(temp_restore_dir)

                print(Fore.GREEN + "Restore completed successfully.")
                any_key_to_continue()
                print()
                log_message("INFO", f"Restore successful for file {restore_file}")

            except Exception as err:
                print(Fore.RED + f"Failed to restore data: {err}")
                any_key_to_continue()
                print()
                log_message("ERROR", f"Failed to restore data: {err}")
                raise

        restore_data(rf)

    except Exception as e:
        log_message("ERROR", f"An error occurred during restore: {e}")
        print(Fore.RED + f"Error: {e}")
        any_key_to_continue()
        print()
