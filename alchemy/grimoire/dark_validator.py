from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    spell = dark_spell_allowed_ingredients()
    if any(item in ingredients.lower() for item in spell):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
