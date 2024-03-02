from weapon import Weapon

def run():
    # Creating two instances of Weapon
    sword = Weapon("Excalibur", "Sword")
    bow = Weapon("Longbow", "Bow")

    # Displaying initial details
    print("Initial Weapon Details:")
    sword.display()
    bow.display()

    # Upgrading weapons
    sword.upgrade()
    bow.upgrade()

    # Displaying upgraded details
    print("\nUpgraded Weapon Details:")
    sword.display()
    bow.display()

if __name__ == "__main__":
    run()
