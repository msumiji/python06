def validate_ingredients(ingredients: str) -> str:
    spell = light_spell_allowed_ingredients()
	if ingrdients in spell:
		return f"{ingredients} - VALID"
	return f"{ingredients} - INVALID"
