import random

husband = ["Justin_Bieber", "Alejandro", "Shawn_Mendes", "Zac_Efron"]
child = ["Poop", "Bobbidibob", "Steve", "Alejandro"]
house = ["camper", "mansion", "tent", "RV"]

random_husband = random.choice(husband)
random_child = random.choice(child)
random_house = random.choice(house)

print("Your husband is " + random_husband)
print("Your child's name will be " + random_child)
print("You will live in a " + random_house)