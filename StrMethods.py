name=input("Enter the name:")
#len()-is used to find the length of the string which includes the whitespaces
Final=len(name)
#find()-is used to find the value and gives the index of that value
#result=name.find("a")
#reverse
result=name.rfind("a")
#capitalize()-will make the first letter capital
rek=name.capitalize()
#upper()-gives all the letter in a string in upper case
nag=name.upper()
#isdigit()-check whether the string contains only the number or not
nar=name.isdigit()
#isalpha()-checks whether the string contains only the string 
man=name.isalpha()
#count()-is used to count the occurance
ban=name.count("a")
#replace(Current,to be replaced)-is used to replace the variable
aji=name.replace("n","s")
print(Final)
print(result)
print(rek)
print(nag)
print(nar)
print(man)
print(ban)
print(aji)
print(help(str))