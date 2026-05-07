states = ("Maryland", "Virginia", "Delaware", "Pennsylvania", "New York")
print(f"Total states: {len(states)}")


print(f"First state: {states[0]}")
print(f"Last state: {states[-1]}")

print(f"New York in states: {'New York' in states}")

print(f"states sorted: {sorted(states)}")

max(len(state) for state in states)
print(f"Longest state name length: {max(len(state) for state in states)}")