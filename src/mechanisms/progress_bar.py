from colorama import Fore, Style


def display_progress_bar(progress, total, bar_length=40):
    percent = progress / total
    filled_length = int(bar_length * percent)
    bar = f"{Fore.GREEN}{"=" * filled_length}{Style.RESET_ALL}{"-" * (bar_length - filled_length)}"
    print(f"\rProgress: [{bar}] {progress}/{total} files ({percent * 100:.2f}%)", end="", flush=True)