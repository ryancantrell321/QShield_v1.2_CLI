import colorama as cl
from src.texts.texts import t1, t2, t3, t4
from src.mechanisms.text_wrap import justify_text, terminal_width

try:
    print()
    print(cl.Fore.GREEN + justify_text(t1, terminal_width))
    print(cl.Style.RESET_ALL)

    print(cl.Fore.GREEN + justify_text(t2, terminal_width))
    print(cl.Style.RESET_ALL)

    print(t3)
    print()

    while True:
        print(cl.Fore.YELLOW + justify_text(t4, terminal_width))
        print(cl.Style.RESET_ALL)

        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            from src.mechanisms.backup import backup
            backup()

        elif choice == 2:
            from src.mechanisms.restore import restore
            restore()
        elif choice == 3:
            from src.mechanisms.usage import usage
            usage()
        elif choice == 4:
            from src.mechanisms.logs import logs
            logs()
        elif choice == 5:
            print("Exiting QShield...")
            break

        break


except Exception as e:
    print(f"Error: {e}")
