"""
circle_area.py — calculates the area of a circle.
Formula: A = π * r²
Cris Ramiez — 4/26/2026
"""

import math          # stdlib — gives us math.pi

ROUND_DIGITS = 4     # decimal places for the result


def calculate_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2


def get_radius():
    """Prompt the user for a radius and validate input."""
    while True:
        try:
            r = float(input("Enter radius: "))
            return r
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Orchestrate: get input, compute, display result."""
    radius = get_radius()
    area = calculate_area(radius)
    print(f"Area = {round(area, ROUND_DIGITS)}")


if __name__ == "__main__":
    main()