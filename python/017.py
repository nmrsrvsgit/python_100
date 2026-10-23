#shopping bill calculator
Q=int(input("Enter quantity:"))
P=float(input("Enter price per item:"))
d=float(input("Enter discount:"))
total=Q*P
discount_amt=(total*d)/100
Final_Bill=total-discount_amt
print(f"total={total}")
print(f"discount amt={discount_amt}")
print(f"Final bill={Final_Bill}")
