#college exam result system
class RegularStudent:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def calculate_final_marks(self):
        return self.marks   

class Sports_student(RegularStudent):
    def __init__(self, name, marks):
        super().__init__(name, marks)

    def calculate_final_marks(self):
        return min(self.marks + 5, 100)
    
R1=RegularStudent("Rahul",43)
S1=Sports_student("Priya",98)
print("Regular student marks:", R1.calculate_final_marks()) 
print("Sports student marks: ",S1.calculate_final_marks())   