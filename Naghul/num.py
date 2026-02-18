'''
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
if(a>b)and(a>c):
    print("A is bigger")
elif(a<b)and(c<b):
    print("B is bigger")
else:
    print("c is bigger")
'''
'''
a=int(input("Enter the number:"))
if(a%2==0):
    print("A is an even number")
else:
    print("A is an odd number")
'''
'''
a=int(input("Enter the year"))
if(a%4==0):
    print("A is an leap year")
else:
    print("A is an non leap year")
'''

a=float(input("Enter the height"))
b=int(input("Enter the height"))
if(a>=4)and(a<5):
    if(b>=55)and(b<65):
        print("You are fit")
    elif(b>=65):
        print("You are overweight")
    else:
        print("you are underweight")
elif(a>=5)and(a<6):
    if(b>=65)and(b<75):
        print("You are fit")
    elif(b>=75):
        print("You are overweight")
    else:
        print("you are underweight")
elif(a>=6)and(a<7):
    if(b>=75)and(b<85):
        print("You are fit")
    elif(b>=85):
        print("You are overweight")
    else:
        print("you are underweight")
else:
    print("Invalid Number!!!!")
