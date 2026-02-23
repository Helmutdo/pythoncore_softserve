def format_string(s):
    """Return string with proper capitalization and single spaces."""
    normalized = " ".join(s.split())
    return normalized.capitalize() if normalized else normalized
