class Order:
    def delivery_charge(self):
        return 40
class Premium_order(Order):
        def delivery_charge(self):
             return 0
O1 = Order()
P1 = Premium_order()
print(O1.delivery_charge())
print(P1.delivery_charge())        
