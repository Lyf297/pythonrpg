import time
import os

def type_effect(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def banner():
    art = r"""
████████╗███████╗██████╗ ██████╗ ██╗███████╗███████╗
╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║██╔════╝██╔════╝
   ██║   █████╗  ██████╔╝██████╔╝██║█████╗  █████╗  
   ██║   ██╔══╝  ██╔═══╝ ██╔═══╝ ██║██╔══╝  ██╔══╝  
   ██║   ███████╗██║     ██║     ██║███████╗███████╗
   ╚═╝   ╚══════╝╚═╝     ╚═╝     ╚═╝╚══════╝╚══════╝
          THE FORGOTTEN HERO
"""
    type_effect(art,0.002)
    type_effect("🌌 Selamat datang di dunia Terminal Quest! 🌌\n",0.03)