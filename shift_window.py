
import pyautogui as pag
import argparse


def shift_right():
    pag.hotkey("ctrl", "alt", "right")


def shift_left():
    pag.hotkey("ctrl", "alt", "left")


def create_terminal():
    pag.hotkey("ctrl", "alt", "t")

def create_terminal_and_command(command):
    # Open terminal 
    pag.hotkey("ctrl", "alt", "t")


def main():
    parser = argparse.ArgumentParser(description="Example screipt using argparse.")

    # Positional argument
    parser.add_argument(
        "-r", action="store_true", help="Moves the current window right."
    )
    parser.add_argument(
        "-l", action="store_true", help="Moves the current window left."
    )
    parser.add_argument("-t", action="store_true", help="opens a new terminal")
    parser.add_argument("-tc", help="opens a new terminal and calls the specified command", type=str)
    args = parser.parse_args()
    if args.r:
        shift_right()
    if args.l:
        shift_left()
    if args.t:
        create_terminal()
    if args.tc:
        create_terminal_and_command(args.tc)

if __name__ == "__main__":
    main()
