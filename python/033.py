class Employee:
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id

class Developer(Employee):
    def __init__(self,name,employee_id,language):
        self.language=language
        super().__init__(name,employee_id)    
    def display_details(self):
        print("Name:",self.name)
        print("Employee id:",self.employee_id)
        print("language:",self.language)       

E1=Developer("Rahul",121,"Python")  
E1.display_details()      