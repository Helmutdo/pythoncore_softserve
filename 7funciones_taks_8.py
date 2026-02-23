def zero_fuel(distance_to_pump, mpg, fuel_left):
    """Return True if fuel is enough to reach the pump."""
    return fuel_left * mpg >= distance_to_pump
