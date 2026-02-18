unit=input("Enter the unit whether celsius or farenheit!!!(C/F):")
temp=float(input("Enter the current temperature of your location"))
if(unit=="C"):
    f=(9/5*temp)+32
    print(f"Your temperature in farenheit is{round(f,2)}°F")
elif(unit=="F"):
    c=(temp-32)*5/9
    print(f"Your temperature in Celsius is{round(c,2)}°C")
else:
    print(f"Please enter the unit!!!")