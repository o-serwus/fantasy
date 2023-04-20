import random

def char_class():
    one_class = ""
    one_class_pos = random.randint(1,3)
    if(one_class_pos == 1):
        one_class = "Barbarian"
    elif(one_class_pos == 2):
        one_class = "Druid"
    else:
        one_class = "Cleric"
        
    return one_class


print("Welcome to the character generator!")
character_no = int(input("How many characters are we creating: "))

char_range = range(0, character_no)

name_list = []

for char in char_range:
    player_name = input("Give me a name: ")
    name_list.append(player_name)
    
print("Let's name the brave adventurers: ")

char_counter = 1

for name in name_list:
    p_class = char_class()
    print(f"{name} is a {p_class}")
    one_strength = random.randint(3, 15)
    one_health = random.randint(3, 15)
    one_magic = random.randint(3, 15)
    one_initiative = random.randint(3, 15)
    
    if(p_class == "Barbarian"):
        one_strength *= 3
        one_health *= 3
    elif(p_class == "Druid"):
        one_magic *= 2
        one_initiative *= 2
        one_health *= 2
    else:
        one_magic *=3
        one_initiative *=3
        
    print("Strength", one_strength)
    print("Magic", one_magic)
    print("Health", one_health)
    print("Initiative", one_initiative)
    print("------------------------")

print("Happy adventuring!")
