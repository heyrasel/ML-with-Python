# def myFunction(): # def er mane define kora 
#     print("My name is Rasel")

# myFunction()
# myFunction()




# def fullName(first_name, last_name): # parenthesis er moddhe egula parameter pass korbo
#     print(first_name+" "+ last_name)

# fname = input("Enter your first name: ")
# lname = input("Enter your last name: ")
# fullName("Your full name is: "+fname, lname)





# def myCountry(country = "Bangladesh"): # Here value pass na korle by default BD dekhabe
#     print(f"My country is {country}")

# myCountry("ABC") # as ABC dichi so default ta mane BD ta ekhn dekhabe na





def calculator(value, sign):
    if(sign=='+'):
        return value + 15
    if(sign=='*'):
        return value * 15
    
print(calculator(13,'*'))
