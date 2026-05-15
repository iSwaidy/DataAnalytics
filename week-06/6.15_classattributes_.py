# Cris Ramirez
# Define a Python class with class attributes

print()
# Create a class named Student
class Student:

    # Class attribute
    school = "YearUp United"

    # Constructor method
    def __init__(self, name, grade):
        # Instance attributes
        self.name = name
        self.grade = grade

    # Method to display student information
    def display_info(self):
        print(f"School: {Student.school}")
        print(f"Student Name: {self.name}")
        print(f"Grade: {self.grade}")
        print("--------------------")


# Create 2 student objects
student1 = Student("Alice", 95)
student2 = Student("Brian", 88)

# Display student information
student1.display_info()
student2.display_info()