import json
import random
import os
from utils import type_effect, clear_screen, banner
from player import Player
from battle import battle
from shop import shop
from story import story_data, start_story

SAVE_FILE = "save_data.json"

def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            return Player.from_dict(data)
    return None

def save_game(player):
    with open(SAVE_FILE, "w") as f:
        json.dump(player.to_dict(), f)

def main():
    clear_screen()
    banner()
    player = load_game()
    if player:
        type_effect(f"Selamat datang kembali, {player.name}!\n",0.03)
    else:
        name = input("Masukkan nama karaktermu: ")
        player = Player(name)
        type_effect(f"\nSelamat datang, {player.name}...\n",0.03)
        start_story(player)

    current_point = "start"
    while True:
        point = story_data.get(current_point)
        if not point:
            type_effect("Error: story point tidak ditemukan.\n",0.03)
            break

        type_effect("\n" + point.get("text",""),0.03)

        # Efek langsung
        effect = point.get("effect")
        if effect:
            for k,v in effect.items():
                setattr(player,k,getattr(player,k)+v)
                if k=="hp":
                    player.hp = min(player.hp, player.max_hp)

        # Battle
        if point.get("battle"):
            battle(player, point["battle"])

        # Ending
        if point.get("ending"):
            type_effect(f"\n=== ENDING: {point['ending'].upper()} ===\n",0.05)
            break

        # Pilihan
        choices = point.get("choices")
        if choices:
            for key,text in choices.items():
                print(f"{key}. {story_data[text]['choice_text']}")
            choice = input("Pilih aksi: ")
            if choice in choices:
                current_point = choices[choice]
            else:
                type_effect("Pilihan tidak valid, coba lagi.",0.03)
        else:
            current_point = point.get("next")
            if not current_point:
                type_effect("Petualangan berakhir.",0.03)
                break

        # Menu Cepat
        print("\n🏕️ Menu Cepat: 1.Bertarung 2.Toko 3.Status 4.Simpan & Keluar")
        quick = input("Pilih (atau enter untuk lanjut cerita): ")
        if quick=="1":
            battle(player)
        elif quick=="2":
            shop(player)
        elif quick=="3":
            player.show_status()
        elif quick=="4":
            save_game(player)
            type_effect("Progress tersimpan. Sampai jumpa!\n",0.03)
            break

if __name__ == "__main__":
    main()