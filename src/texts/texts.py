from src.mechanisms.times import get_current_year


t1 = """Pandora QShield v1.2_CLI is a command-line utility tool that enables end-users to effortlessly back up and restore their qBittorrent data.\nSupports Windows 8.1/10/11 for now. Cross-Platform support planned for the future."""
t2 = f"""©{get_current_year()} Pandora Dynamics, RyanCantrell321. All Rights Reserved!"""
t3 = """License: GNU General Public License (GPL) 3.0 | https://www.gnu.org/licenses/gpl-3.0.en.html#license-text"""
t4 = """\nOptions:\n1. Backup qBittorrent Data \n2. Restore qBittorrent Data \n3. View Usage Guide\n4. View Logs\n5. Contact Support (GitHub page will be opened)\n6. Exit QShield"""
t5 = """Invalid choice. Please enter a valid option."""


def display():
    print()
    print(t1)
    print()
    print(t2)
    print(t3)
    print()
