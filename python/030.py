
class Student:
    #class variable
    program_name= "python problem solving"

    #constructor
    def __init__(self,name,roll,attendance):
        self.name= name
        self.roll= roll
        self.attendance= attendance

     #Instance method
    def display_details(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Attendance:", self.attendance)

     #Instance method   
    def check_eligibility(self):
        if self.attendance>=70:
            print("Eligible for assessment")
        else:
            print("Not eligible for assesment")

    #class method
    @classmethod
    def display_program(cls):
        print("Training program:",cls.program_name)

s1 = Student("Rahul", 101, 85)
s2 = Student("Priya", 102, 70)
s3 = Student("Aman", 103, 90)
s4 = Student("Neha", 104, 60)     

Student.display_program()


for student in [s1, s2, s3, s4]:
    print("\n-------------------")
    student.display_details()
    student.check_eligibility()
