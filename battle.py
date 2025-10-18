import random
import json
from utils import type_effect

with open("monsters.json") as f:
    MONSTERS = json.load(f)

def battle(player, monster_name=None):
    if not monster_name:
        monster_name = random.choice(list(MONSTERS.keys()))
    monster_hp = MONSTERS[monster_name]["hp"]
    monster_atk = MONSTERS[monster_name]["atk"]

    type_effect(f"\nSeekor {monster_name} muncul! HP:{monster_hp} ATK:{monster_atk}\n",0.03)

    while monster_hp>0 and player.hp>0:
        print("1. Serang 2. Lari")
        choice = input("Pilihanmu: ")
        if choice=="1":
            dmg = max(player.atk - random.randint(0,2),1)
            monster_hp -= dmg
            type_effect(f"Kamu menyerang {monster_name} dan memberikan {dmg} damage!\n",0.03)
            if monster_hp<=0:
                gold_reward = random.randint(5,20)
                player.gold += gold_reward
                type_effect(f"{monster_name} kalah! Kamu mendapatkan {gold_reward} gold.\n",0.03)
                break
            dmg_taken = max(monster_atk - player.defense,1)
            player.hp -= dmg_taken
            type_effect(f"{monster_name} menyerang balik dan memberikan {dmg_taken} damage!\n",0.03)
        elif choice=="2":
            if random.random()>0.5:
                type_effect("Kamu berhasil kabur!\n",0.03)
                break
            else:
                dmg_taken = max(monster_atk - player.defense,1)
                player.hp -= dmg_taken
                type_effect(f"Gagal kabur! {monster_name} menyerang dan memberikan {dmg_taken} damage.\n",0.03)
        else:
            type_effect("Pilihan tidak valid!\n",0.03)
    if player.hp<=0:
        type_effect("Kamu kalah dalam pertarungan...\nGame Over.\n",0.05)
        exit()