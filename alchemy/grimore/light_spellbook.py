def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]

def light_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if "INVALID" in result:
        return Spell rejected"
    return f"Spell recorded: {spell name} ({result})"
