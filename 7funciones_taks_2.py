def distance(p1, p2):
    """Calculate distance between two ordered pairs. O(1)."""
    return round(((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5, 2)
