## Cris Ramirez


student_name = input("Student name: ")
student_major = input("Major code (BIOL, CSCI, ENG, HIST, MKT): ").upper()

#  Use if-elif-else statements to determine the major name and location
if student_major == "BIOL":
    major_name = "Biology"
    location = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major_name = "Computer Science"
    location = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major_name = "English"
    location = "Kerr Hall, Room 201"
elif student_major == "HIST":
    major_name = "History"
    location = "Kerr Hall, Room 114"
elif student_major == "MKT":
    major_name = "Marketing"
    location = "Westly Hall, Room 310"
else:
    major_name = "<unknown>"
    location = ""

# Print the results
print(f"{student_name} — Major: {major_name}")
print(f"Department Office: {location}")