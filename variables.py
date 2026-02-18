#--Strings
#An f-string (formatted string literal) is an easy and readable way to insert variables and 
# expressions inside a string in Python.
first_name="Naghul"
Food="Briyani"
Hobby="Skating"
print(f"Hello {first_name}")
print(f"I like {Food}")
print(f"My hobby is {Hobby}")

#--Integers
roll_number=50
print(f"My roll number is {roll_number}")
# or 
print("my roll number is:",roll_number)

#Float
cost=10.34
gpa=8.458
print(f"the price is:{cost}")
print(f"My gpa is:{gpa}")

#Boolean
is_student=True
if is_student:
    print("You are a student")
else:
    print("You are not the student")