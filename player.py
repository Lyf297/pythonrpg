class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 20
        self.max_hp = 20
        self.atk = 5
        self.defense = 2
        self.gold = 0
        self.equipment = {"weapon":"Iron Sword","armor":"Leather Armor"}

    def show_status(self):
        print(f"\n=== STATUS {self.name} ===")
        print(f"Level: {self.level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"ATK: {self.atk}")
        print(f"DEF: {self.defense}")
        print(f"Gold: {self.gold}")
        print(f"Weapon: {self.equipment['weapon']}")
        print(f"Armor: {self.equipment['armor']}")
        print("="*30)

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        player = cls(data['name'])
        player.level = data['level']
        player.hp = data['hp']
        player.max_hp = data['max_hp']
        player.atk = data['atk']
        player.defense = data['defense']
        player.gold = data['gold']
        player.equipment = data['equipment']
        return player