from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    spell = light_spellbook.light_spell_allowed_ingredients()
    if any(item in ingredients.lower() for item in spell):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
