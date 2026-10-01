import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
result = alchemy.create_air()
print(f"Testing create_air: {result}")
print("Now show that not all functions can be reached")
print("This will raise an exception!")
print("Testing the hiden create earth:", end="")
result = alchemy.create_earth()
