def validate_fighter_data(data: dict) -> list[str]:
    errors = []
    if not data.get("first_name"):
        errors.append("First name is required.")
    if not data.get("gender") in ["Male", "Female"]:
        errors.append("Gender must be Male or Female.")
    # Add more checks...
    return errors