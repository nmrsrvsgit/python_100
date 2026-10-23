# A small shop wants to represent products using objects. Every product has: • product name • price • quantity Create a class named Product. The constructor should receive these three values. Create a method that displays Product Name, Price, Quantity and Total Price. Total Price = Price x Quantity Create at least three product objects. Example data: Laptop Mouse - 500 - 2 Keyboard - 900 - 1 Pendrive - 700 - 3
class Product:
    def __init__(self,product_name,price,quantity):
        self.product_name= product_name
        self.price= price
        self.quantity=quantity
    def display_details(self):
        total_price=self.price*self.quantity
        print("Product name:",self.product_name)
        print("price:" ,self.price)
        print("Quantity:",self.quantity)
        print("total_price:",total_price)
p1=Product("Laptop",500,2)
p2=Product("Mouse",100,3)
p3=Product("Keyboard",700,1)

p1.display_details()
p2.display_details()
p3.display_details()