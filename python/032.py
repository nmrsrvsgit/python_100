# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")
        
# d1=Dog()
# d1.eat()
# d1.bark()

class Person:
    def __init__(self,name):
        self.name=name
          
    def show_name(self):
        print("Name:",self.name)

class Student(Person):
    def __init__(self, name,rollno):
        self.rollno=rollno
        super().__init__(name)

    def display_details(self):
        print("Name:",self.name) 
        print("Rollno:",self.rollno)   
s1=Student("rahul",101)
s1.show_name()
s1.display_details()       