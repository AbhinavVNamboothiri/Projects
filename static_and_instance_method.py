class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"Name: {self.name}, Position: {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer", "Admin"]
        return position in valid_positions

employee1 = Employee("John", "Manager")
employee2 = Employee("Jane", "Designer")
employee3 = Employee("Bob", "Admin")
employee4 = Employee("Alice", "Developer")
employee5 = Employee("Tom", "CEO")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())
print(employee5.get_info())

print(Employee.is_valid_position("Manager"))
print(Employee.is_valid_position("CEO"))
    
    