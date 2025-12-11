class student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.total_gpa += gpa

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return cls.total_gpa / cls.count

student1 = student("John", 4.0)
student2 = student("Jane", 3.5)
student3 = student("Bob", 3.0)
student4 = student("Alice", 2.5)
student5 = student("Tom", 2.0)

print(student.get_average_gpa())