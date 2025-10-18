import time
import os

def type_effect(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")