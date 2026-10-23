class Employee:
    def __init__(self,name,basic_salary):
        self.name = name
        self.basic_salary= basic_salary

    def calculate_salary(self):
        return self.basic_salary
class Developer(Employee):
    def calculate_salary(self):
        return self.basic_salary + 5000
E1= Employee("Rahul",10000)    
D1= Developer("Suraj",30000)

print("Employee Name:", E1.name)
print("Employee Salary:", E1.calculate_salary())

  
print("Developer Name:", D1.name)
print("Developer Salary:", D1.calculate_salary())
