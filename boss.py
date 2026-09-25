from enemy import Enemy


class Boss(Enemy):
    """A stronger enemy with a powered-up attack."""

    def __init__(self, name):
        super().__init__(name, health = 250, attackPower = 30)

    def health(self):
        health = self.health()
        bonus_health = 7
        print(f"{self.name} drank health posession")
        
        return health + bonus_health


    def attack(self):
        damage = super().attack()
        bonus_damage = 5
        print(f"{self.name} unleashes a crushing blow!")
        return damage + bonus_damage