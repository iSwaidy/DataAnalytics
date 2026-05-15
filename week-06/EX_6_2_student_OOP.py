# Cris Ramirez
# Student Roster Manager
# Concepts: class, objects, encapsulation, getters, setters

class Student:
    # Class attribute (shared by all students)
    school = "YearUp Academy"

    # Constructor - instance attributes
    def __init__(self, name, grade, track):
        self.name    = name          # public
        self.__grade = grade         # private (encapsulated)
        self.track   = track         # public

    # -- GETTER -----------------------------------------------
    def get_grade(self):
        return self.__grade

    # -- SETTER (with validation) -----------------------------
    def set_grade(self, new_grade):
        try:
            if 0 <= new_grade <= 100:
                self.__grade = new_grade
            else:
                print("❌ Invalid grade! Must be 0–100.")
        except TypeError:
            print("❌ Invalid input! Grade must be a number.")

    # -- DISPLAY METHOD ---------------------------------------
    def display_info(self):
        print(f"""
===== YearUp Academy — Student Report =====
School : {Student.school}
Name   : {self.name}
Grade  : {self.get_grade()}
Track  : {self.track}
===========================================""")

    # -- AVERAGE GRADE CLASS METHOD ---------------------------
    @classmethod
    def average_grade(cls, students):
        total = sum(s.get_grade() for s in students)
        return total / len(students)


# -- Create student objects -----------------------------------
student1 = Student("Alice", 95, "Software Development")
student2 = Student("Brian", 88, "Data Analytics")

# -- Getter: read the private grade ---------------------------
print(student1.get_grade())   # 95
print(student2.get_grade())   # 88

# -- Setter: valid and invalid updates ------------------------
student1.set_grade(98)        # valid — updates to 98
student1.set_grade(150)       # invalid — blocked
student1.set_grade("ninety")  # TypeError — blocked by try/except

# -- Call display methods -------------------------------------
student1.display_info()
student2.display_info()

# -- Average grade across all students ------------------------
all_students = [student1, student2]
print(f"\nClass Average: {Student.average_grade(all_students):.2f}")

# -- Input-driven student creation ----------------------------
print("\n--- Add a New Student ---")
name  = input("Student name: ")
track = input("Student track: ")
grade = int(input("Starting grade: "))
student3 = Student(name, grade, track)
student3.display_info()