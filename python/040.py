#E-COMMERCE DISCOUNT SYSTEM
class NormalCustomer:
    def __init__(self,name,pro_price):
        self.name = name
        self.pro_price = pro_price

    def calculate_payamt(self):
     return self.pro_price

class PremiumCustomer(NormalCustomer):
    def __init__(self, name, pro_price):
       super().__init__(name, pro_price)

    def calculate_payamt(self):
       discount = self.pro_price*10 / 100
       payable_amount = self.pro_price - discount
       return payable_amount

N1 = NormalCustomer("Priya",2000)
P1 = PremiumCustomer("Rahul",2000)

print("Normal Customer:", N1.name)
print("Payable Amount:", N1.calculate_payamt())

print("Premium Customer:", P1.name)
print("Payable Amount:", P1.calculate_payamt())
           
    
        
        