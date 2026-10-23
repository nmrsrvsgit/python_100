#student marks and percentage
sub1=int(input("Enter subject1 marks:"))
sub2=int(input("Enter subject2 marks:"))
sub3=int(input("Enter subject3 marks:"))
total=sub1+sub2+sub3
percentage = (total/300)*100
print(f"Percentage:{percentage}%")