class Order:
    delivery_charge=  50
    def __init__(self,orderID,customer_name,product,price,quantity):
         self.orderID=orderID
         self.customer_name=customer_name
         self.product= product
         self.price= price
         self.quantity=quantity

    def display_bill(self):
        product_amount = self.price * self.quantity
        final_amount = product_amount + Order.delivery_charge

        print("\n----- ORDER BILL -----")
        print("Order ID:", self.orderID)
        print("Customer Name:", self.customer_name)
        print("Product:", self.product)
        print("Price per item: Rs.", self.price)
        print("Quantity:", self.quantity)
        print("Product Amount: Rs.", product_amount)
        print("Delivery Charge: Rs.", Order.delivery_charge)
        print("Final Amount: Rs.", final_amount)

    def check_quantity(self):
        if self.quantity > 0:
            print("Valid quantity")
        else:
            print("Invalid quantity")


order1 = Order(101, "Rahul", "Laptop", 50000, 1)
order2 = Order(102, "Priya", "Headphones", 1500, 2)

order1.display_bill()
order1.check_quantity()

order2.display_bill()
order2.check_quantity()
   