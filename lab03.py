import random

# Dice Option created using list() and range()
diceOptions = list(range(1,7))

# Weapons list
weapons = ["First", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

print("Available Weapons are: ", ','.join(weapons))

def getCombatStrength(prompt):
    while True:
        value = input(prompt)
        if 1 <= value <= 6:
            return value
        else:
            print("Invaild Input! Please enter a number between 1-6")

CombatStrength = getCombatStrength("Please enter a number between 1 and 6 for Players")
mCombatStrength = getCombatStrength("Please enter a number between 1 and 6 for Monster")    

for j in range(1, 21, 2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll - 1]
    monsterWeapon = weapons[monsterRoll - 1]

    heroTotal = CombatStrength + heroRoll
    monsterTotal = mCombatStrength + monsterRoll

    print(f"\n Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"\n Hero selected {heroWeapon}, Monster selected{monsterWeapon}")
    print(f"\n Hero Total Strength: {heroTotal}, Monster Total Strength: {monsterTotal}")

    if heroTotal > monsterTotal:
        print("Player Wins!")
    elif heroTotal < monsterTotal:
        print("Monter Wins!")
    else: 
        print("It's a tie!")

if j != 11:
    print("Battle concluded after 20 rounds!")        