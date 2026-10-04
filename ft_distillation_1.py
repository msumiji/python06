import alchemy

print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
result1 = alchemy.strength_potion()
print(f"Testing strength_potion: {result1}")
result2 = alchemy.heal()
print(f"Testing heal alias: {result2}")
