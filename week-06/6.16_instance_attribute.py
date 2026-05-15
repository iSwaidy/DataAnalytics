# Define a Python class with instance attributes

print()
# Create a class named Student
class Student:

    # Class attribute (shared by all students)
    school = "YearUp United"

    # Constructor method
    def __init__(self, name, grade, track):
        # Instance attributes (unique for each object)
        self.name = name
        self.grade = grade
        self.track = track

    # Method to display student information
    def display_info(self):
        print(f"School: {Student.school}")
        print(f"Student Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"Track: {self.track}")
        print("--------------------")

# Create student objects
student1 = Student("Alice", 95, "Software Development")
student2 = Student("Brian", 88, "Data Analytics")

# Display instance attributes directly
print(f"{student1.name} is in the {student1.track} track.")
print(f"{student2.name} is in the {student2.track} track.")

print()

# Call methods
student1.display_info()
student2.display_info()