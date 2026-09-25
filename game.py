from hero import Hero
from goblin import Goblin
from boss import Boss



ARENA_NAME = "The Iron Circle"
def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero.damage = hero.attck()
        enemy.take_damage(hero.damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)

    if hero.is_alive():
        print(f"(hero.name) wins!")
    else:
         print(f"(enemy.name) wins!")





def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Bibble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    
    goblinTwo = Goblin("Wiggle")

    print(f"{goblinTwo.name} enters the arena with {goblinTwo.health} health.")

    Rowan = Hero("Rowan")

    print(f"Oh my goodness {Rowan.name} the {Rowan.role} enters the arena with {Rowan.health} health!!")

    heroDamage = Rowan.attack()

    goblin.take_damage(heroDamage)

    bossGuy = Boss("Phil")

if __name__ == "__main__":
    main()
