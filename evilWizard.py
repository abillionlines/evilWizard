import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power, special, special2, heal):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
        self.special = special
        self.special2 = special2
        self.heal = heal

    def attack(self, opponent):
        min_damage = self.attack_power - 5
        max_damage = self.attack_power + 5
        actual_damage = random.randint(min_damage, max_damage)
        opponent.health -= actual_damage
        print(f"{self.name} attacks {opponent.name} for {actual_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def useSpecial(self, opponent):
        opponent.health -= self.special
        print(f"{self.name} attacks {opponent.name} with the {self.special1} for {self.special}")
        
        
    def healing(self):
        self.health += self.heal
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals themselves. Current health: {self.health}/{self.max_health}.")
    
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, special=80, special2=0, heal=20)
    special1: str = "Deafening Screams"
    special2_name: str = "Evade"
    special2_name2: str = "evade"
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, special=70, special2=0, heal=30)
    special1: str = "Cascading Ice Sheets"
    special2_name: str = "Divine Shield"
    special2_name2: str = "find shelter from"
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, special=0, special2=0, heal=0)
     
    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        
    
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=270, attack_power=30, special=50, special2=0, heal=40)
    special1: str = "Angry Mother Mob"
    special2_name: str = "Turtle Shell"
    special2_name2: str = "hide from"    
    
class Paladin(Character):
    def __init__(self, name) :
        super().__init__(name, health=270, attack_power=10, special=60, special2=0, heal=20)
    special1: str = "Calculated Risk"
    special2_name: str = "Anti Matter Evasion"  
    special2_name2: str = "Evade"
    
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name) 
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        is_evading = False
        print("\n--- Your Turn ---")
        print("1. Attack")
        print(f"2. {player.special1}")
        print(f"3. {player.special2_name}")
        print("4. Heal")
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.useSpecial(wizard)
        elif choice == '3':
            print(f"{player.name} prepares to {player.special2_name2} the next attack!")
            is_evading = True  
        elif choice == '4':
            player.healing()
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            
          
            if is_evading:
                print(f"{wizard.name} attacks {player.name}, but {player.name} dodges it gracefully!")
            else:
                wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
