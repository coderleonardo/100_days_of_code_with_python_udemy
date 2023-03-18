################### Scope ####################

enemies = 1

def increase_enemies():
    global enemies # do not do this, just if you really need
    enemies += 1
    print(f"enemies inside function: {enemies}")

print(f"enemies outside function: {enemies}")
increase_enemies()


###############################################

# Local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# Global scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()

# There is no Block Scope in Python 
level = 3

enemies = ['1', '2', '3']

if level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# Global constants
PI = 3.14 # upper case


