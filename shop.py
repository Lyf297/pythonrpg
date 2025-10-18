from utils import type_effect

def shop(player):
    items = [
        {"name":"Potion", "price":10, "effect":"heal"},
        {"name":"Steel Sword", "price":30, "effect":"atk"},
        {"name":"Iron Armor", "price":25, "effect":"def"}
    ]
    print("\n🏪 Toko Desa")
    for i,item in enumerate(items,1):
        print(f"{i}. {item['name']} - {item['price']} gold")
    print("4. Keluar")

    choice = input("Beli item (nomor): ")
    if choice in ["1","2","3"]:
        item = items[int(choice)-1]
        if player.gold >= item['price']:
            player.gold -= item['price']
            if item['effect']=="heal":
                player.hp = min(player.max_hp, player.hp + 10)
                type_effect("Kamu meminum Potion. HP bertambah 10!\n",0.03)
            elif item['effect']=="atk":
                player.atk += 2
                player.equipment['weapon'] = item['name']
                type_effect(f"Kamu membeli {item['name']}! ATK bertambah.\n",0.03)
            elif item['effect']=="def":
                player.defense += 2
                player.equipment['armor'] = item['name']
                type_effect(f"Kamu membeli {item['name']}! DEF bertambah.\n",0.03)
        else:
            type_effect("Goldmu tidak cukup!\n",0.03)
    else:
        type_effect("Keluar dari toko.\n",0.03)