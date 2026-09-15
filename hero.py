import random
class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self,name):
        self.name = name # name changes for each hero created
        self.health = 100 # evry hero has 100 health
        self.attack_power = 20 # every hero has 20 attack power
        self.role = "mage"

    def attack(self):
        return random.randint(0, self.attack_power)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0




    pass
