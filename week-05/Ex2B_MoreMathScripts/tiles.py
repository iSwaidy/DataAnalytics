## Cris Ramirez


import math

length = 12
width = 10
tiles_needed = length * width  # 1 tile per square foot
tiles_with_extra = tiles_needed * 1.10   # Add 10% extra for breakage and cuts
boxes = math.ceil(tiles_with_extra / 12) # Each box contains 12 tiles

print(f"Room is {length} x {width} feet")
print(f"Tiles needed (with 10% extra): {tiles_with_extra}")
print(f"Boxes to buy: {boxes}")