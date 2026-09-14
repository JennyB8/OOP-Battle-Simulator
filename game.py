from hero import Hero
from goblin import Goblin



ARENA_NAME = "The Iron Circle"


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

    print(f"{Rowan.name} enters the arena with {Rowan.health} health.")

    heroDamage = Rowan.attack()

    goblin.take_damage(heroDamage)

if __name__ == "__main__":
    main()
