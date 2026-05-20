# Cris Ramirez
# Exercise 4.A Lab 1 - Reading Files

f = open('about_me.txt', 'r')

# Experiment 1 - read entire file
# print(f.read())

# Experiment 2 - read in 50-char chunks
# print(f.read(50))
# print(f.read(50))

# Experiment 3 - readline
# print(f.readline(10))
# print(f.readline())

# Experiment 4 - readline in a loop
for i in range(1, 5):
    print(f.readline())

f.close()

# ===========================================================

f = open('about_me.txt', 'r')

first_50 = f.read(50)

loop_lines = []
for i in range(4):
    loop_lines.append(f.readline())

last_chunk = f.readlines(100)

f.close()

print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {loop_lines}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {last_chunk}")