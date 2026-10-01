from elements import create_fire, create_water
from alchemy.elements import create_earth, create_air

def healing_potion():
    return(f"Healing potion brewed with '{create_earth()}' and '{create_air()}'")

def strength_potion():
    return(f"Strength potion brewed with and '{create_fire()}' and '{create_water()}'")

#result1 = healing_potion()
#result2 = strength_potion()
#print(result1)
#print(result2)
