# Cris Ramirez
# sort_index() and rank()
# display results in descending order

import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Student": ["Amy", "Bob", "Cara", "Dan"],
    "Score": [80, 95, 79, 91]
}, index=[3,1,2,0])

print("ORIGINAL DATAFRAME")
print(df)

# .....................................................................

# Sort index highest to lowest
print("\nSORTED INDEX (highest to lowest)")
sorted_df = df.sort_index(ascending=False)
print(sorted_df)

# .....................................................................

# Rank by score
df["Rank"] = df["Score"].rank(ascending=False)

# Sort by highest score appears first
print("\nRANKING (highest to lowest)")
print(df.sort_values("Score", ascending=False))