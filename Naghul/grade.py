a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
d=int(input("Enter the number"))
e=int(input("Enter the number"))
total=a+b+c+d+e
avg=total/5
print(total)
print(avg)
if(avg>90)and(avg<=100):
    print("A grade")
elif(avg>75)and(avg<=90):
    print("B grade")
elif(avg>50)and(avg<=75):
    print("c grade")
else:
    print("D grade")

