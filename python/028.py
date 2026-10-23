class Student:
    def __init__(self,name,roll_number,marks):
        self.name= name
        self.roll_number= roll_number
        self.marks= marks
    def display_details(self):
        print("Name:",self.name)
        print("Roll number:",self.roll_number)
        print("Marks:", self.marks)


s1=Student("Raju",101,78)
s2=Student("Priya",102,91)
s3=Student("Aman",103,65)    

s1.display_details()
s2.display_details()
s3.display_details()