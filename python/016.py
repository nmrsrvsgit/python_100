Marks=[23,45,78,89,97,55]
status=["","","","","",""]
i=0
total=0
greatest=Marks[0]
while i<len(Marks):
    total=total+Marks[i]
    if Marks[i]>greatest:
        greatest=Marks[i]
    if Marks[i]>=40:
        status[i]="Pass"
    else:
        status[i]="Fail"     
    i=i+1  
average = total/len(Marks) 
print("Total:", total)
print("Average:", average)
print("Greatest:", greatest)

i = 0

while i < len(Marks):
    print("Mark:", Marks[i], "Status:", status[i])
    i = i + 1 
