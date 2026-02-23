def are_you_playing_banjo(name):
    """Return whether name plays banjo (starts with R or r)."""
    if name[0].lower() == "r":
        return f"{name} plays banjo"
    return f"{name} does not play banjo"
