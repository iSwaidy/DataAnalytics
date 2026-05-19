# Cris Ramirez

try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found. Please check the filename.")