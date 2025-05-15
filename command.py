import time
import pyautogui as pag
import argparse
import subprocess
import os

DEFAULT_TIMING = 1

def shift_right():
    pag.hotkey("ctrl", "alt", "right")


def shift_left():
    pag.hotkey("ctrl", "alt", "left")


def create_terminal():
    pag.hotkey("ctrl", "alt", "t")

def start():
    """This will start a series of applications at startup and open them in specific windows."""
    
    path = os.path.expanduser("~/gh/pyautogui-basic-controls/command.py")

    # Open Calendar
    subprocess.Popen([
            "gnome-terminal", "--", "bash", "-ic",
            f"neo notion-calendar-snap; exec bash"
    ])

    time.sleep(DEFAULT_TIMING)

    # Make calendar fullscreen
    pag.press("F11")
    
    # # Move to a new desktop
    shift_right()
    # pag.hotkey("ctrl","shift","alt", "right")
    # Open thunderbird
    subprocess.Popen([
        "gnome-terminal", "--", "bash", "-ic",
        f"neo thunderbird;"
    ])

    # pag.hotkey("ctrl","shift","alt", "right")
    time.sleep(DEFAULT_TIMING + 1)

    shift_right()
    # time.sleep(DEFAULT_TIMING + 1)
    # Open Notion-Desktop
    subprocess.Popen([
        "gnome-terminal", "--", "bash", "-ic",
        f"neo notion-desktop;"
    ])
    time.sleep(DEFAULT_TIMING)
    # pag.press("F11")
    # pag.hotkey("ctrl","shift","alt", "right")
    # shift_right()
    
    subprocess.Popen([
        "gnome-terminal", "--", "bash", "-ic",
        f"neo firefox;"
    ])
    time.sleep(DEFAULT_TIMING)
    # pag.press("F11")
    # pag.hotkey("ctrl","shift","alt", "right")
    time.sleep(DEFAULT_TIMING + 1)
    pag.hotkey("ctrl","l")
    time.sleep(DEFAULT_TIMING + 1)
    pag.write("https://app.clockify.me/tracker")
    time.sleep(DEFAULT_TIMING + 1)
    pag.press("enter")
    time.sleep(DEFAULT_TIMING + 1)

    shift_right()
    time.sleep(DEFAULT_TIMING + 1)
    subprocess.Popen([
        "gnome-terminal", "--", "bash", "-ic",
        f"neo firefox;"
    ])
    time.sleep(DEFAULT_TIMING + 1)
    pag.press("F11")
    time.sleep(DEFAULT_TIMING + 1)
    pag.write("Good Morning", interval=0.01)
    time.sleep(DEFAULT_TIMING + 1)
    pag.press("enter")
    time.sleep(DEFAULT_TIMING + 1)
    pag.hotkey("ctrl","shift","alt", "right")
    shift_left()
    time.sleep(DEFAULT_TIMING + 1)
    create_terminal()
    time.sleep(DEFAULT_TIMING + 1)
    shift_left()
    
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
    parser.add_argument("--start", action="store_true", help="This drives a series of scripts to open the default applicaitons in default windows.")
    args = parser.parse_args()
    if args.r:
        shift_right()
    if args.l:
        shift_left()
    if args.t:
        create_terminal()
    if args.start:
        start()

if __name__ == "__main__":
    main()
