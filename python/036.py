# class Vehicle:
#     def calculate_rent(self):
#         return 1000
# class car(Vehicle):
#     def calculate_rent(self):
#         return 2000
# v1= Vehicle()
# c1= car()
# print("Vehicle rent:",v1.calculate_rent()) 
# print("Car rent:",c1.calculate_rent())  


class Payment:
    def pay(self):
        print("Processing payment")
class Cashpayment(Payment):
    def pay(self):
        print("paid using cash")
class Cardpayment(Payment):
    def pay(self):
        print("paid using card")
pay1=Payment()
cas1=Cashpayment()
card1=Cardpayment()
pay1.pay()
card1.pay()
cas1.pay()                