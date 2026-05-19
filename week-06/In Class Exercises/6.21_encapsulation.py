# Cris Ramirez
# demonstrates encapsulation

class Student:
    school = "YearUp United"  # Class attribute

    def __init__(self, name, grade, track):
        self.name = name          # Public attribute
        self.__grade = grade      # PRIVATE attribute (encapsulated!)
        self.track = track

    # GETTER - controlled way to READ private grade
    def get_grade(self):
        return self.__grade

    # SETTER - controlled way to UPDATE private grade (with validation)
    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("❌ Invalid grade! Must be between 0 and 100.")

    def display_info(self):
        print(f"School: {Student.school}")
        print(f"Student Name: {self.name}")
        print(f"Grade: {self.__grade}")   # Access private attr inside class
        print(f"Track: {self.track}")
        print("--------------------")

# Create student objects
student1 = Student("Alice", 95, "Software Development")
student2 = Student("Brian", 88, "Data Analytics")

# ❌ This would FAIL - grade is private!
# print(student1.__grade)

# Use the getter instead
print(student1.get_grade())     # Output: 95

# Use the setter to update safely
student1.set_grade(98)          # Works! Valid grade
student1.set_grade(150)         # ❌ Invalid grade! Must be between 0 and 100.

print()
student1.display_info()
student2.display_info()