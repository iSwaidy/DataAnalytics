##Cris Ramirez

movies = ["Spirited Away", "Howl's Moving Castle", "My Neighbor Totoro"]

print(f"The list movies includes my top {len(movies)} favorite movies")
print(movies)

# sorted() creates a new list that is sorted, but leaves the original unchanged.
print(sorted(movies))
print(movies)           # The original list is still in the same order as before.

# .sort() rearranges the list in place. The original is now sorted for good.
movies.sort()
print(movies)

movies.append("Princess Mononoke")
print(f"The list movies includes my top {len(movies)} favorite movies")
print(movies)