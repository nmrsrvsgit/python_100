#Employ management system
class Employee:

    company_name = "Tech solutions"

    def __init__(self,name,employee_id,basic_salary):
        self.name=name
        self.employee_id=employee_id
        self.basic_salary=basic_salary

    def display_details(self):
        print("Name:",self.name)
        print("Employee:",self.employee_id)
        print("Basic slary:",self.basic_salary)    

    def calculate_salary(self):
        return self.basic_salary    
    @classmethod
    def show_company(cls):
        print("company name:",cls.company_name)

    def is_valid_salary(self):
        if self.basic_salary > 0:
            print("Salary is greater than zero")
        else:
            print("salary is zero")   

class Developer(Employee):
    def __init__(self, name, employee_id, basic_salary,language):
        self.language=language
        super().__init__(name, employee_id, basic_salary)
    def display_details(self):
        super().display_details() 
        print("Language:",self.language)
         
    def calculate_salary(self):
        return self.basic_salary + 5000 
E1= Employee("Rahul",101,30000)
D1= Developer("suraj",123,40000,"C++")
E1.display_details()
D1.display_details()
E1.calculate_salary()
D1.calculate_salary()