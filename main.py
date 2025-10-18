import json
import random
import time
import os

from utils import type_effect, clear_screen
from player import Player
from battle import battle
from shop import shop
from story import start_story

SAVE_FILE = "save_data.json"

# Load atau buat player baru
def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            return Player.from_dict(data)
    else:
        return None

def save_game(player):
    with open(SAVE_FILE, "w") as f:
        json.dump(player.to_dict(), f)

def main():
    clear_screen()
    type_effect("🌌 TERMINAL QUEST: THE FORGOTTEN HERO 🌌\n", 0.05)
    player = load_game()
    if player:
        type_effect(f"Selamat datang kembali, {player.name}!\n", 0.03)
    else:
        name = input("Masukkan nama karaktermu: ")
        player = Player(name)
        type_effect(f"\nSelamat datang, {player.name}...\n", 0.03)
        start_story(player)

    while True:
        print("\n🏕️ Desa Awal — Menu Utama")
        print("="*30)
        print("1. Bertarung")
        print("2. Jelajahi Dunia")
        print("3. Toko")
        print("4. Status")
        print("5. Simpan & Keluar")
        print("="*30)
        choice = input("Pilih aksi: ")

        if choice == "1":
            battle(player)
        elif choice == "2":
            type_effect("Kamu menjelajahi dunia...\n", 0.03)
            # Event random sederhana
            event = random.choice(["gold", "trap", "nothing"])
            if event == "gold":
                gold_found = random.randint(5, 20)
                player.gold += gold_found
                type_effect(f"Kamu menemukan {gold_found} gold!\n",0.03)
            elif event == "trap":
                damage = random.randint(1,5)
                player.hp -= damage
                type_effect(f"Ada jebakan! Kamu kehilangan {damage} HP!\n",0.03)
            else:
                type_effect("Petualanganmu lancar tanpa insiden.\n",0.03)
        elif choice == "3":
            shop(player)
        elif choice == "4":
            player.show_status()
        elif choice == "5":
            save_game(player)
            type_effect("Progress tersimpan. Sampai jumpa!\n",0.03)
            break
        else:
            type_effect("Pilihan tidak valid!\n",0.03)

if __name__ == "__main__":
    main()