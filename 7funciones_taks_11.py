def count_sheeps(sheep):
    """Count sheep present (True). Handles None/bad values."""
    return (sheep or []).count(True)
