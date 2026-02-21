# """
# Dictionary is very important.
# It is also important for backend developement.
# It is very fast.
# Its can communicate faster with API
# """

# # 2nd bracket diye dictionary create kora hoy

# guest = {
#     'name': 'Rasel', # Here name holo key and value holo Rasel. Mane key er moddhe value rakha hoy.
#     'age': '25',
#     'favourite_snack': 'Cake'
# }
# print(guest)
# print(guest['name']) # evabe kono loop na chaliye direct value pawa jai

# # f string diyeo print korte pari
# print(f"Name: {guest['name']}, Age: {guest['age']}")

# # Add something in list
# guest["phone_number"] = "01771821343" # Python e single and double qutation doesnt matter for string
# print(guest)

# # # To remove something
# # guest.pop('age') # Age will be removed
# # print(guest)

# # # Another way to remove elements
# # del guest['phone_number']
# # print(guest)

# # # To clear whole dictionary
# # guest.clear()
# # print(guest)





# # loop 
# for keys, value in guest.items(): # keys, value ei 2ta variable. keys ta holo key name and value ta holo value on corresponding keys
#     print(f"{keys} : {value}") # pura dictionary ta dekhte parbo

# # single loop calayeo pawa jabe, but tokhn only key or value pawa jabe, 2ta eksathe pawa jabe na
# for item in guest:
#     # print(item) # only key gula dekhte parbo
#     print(guest[item]) # only value gula dekhte parbo






# Nested dictionaries

party_guest = {
    "guest1": {"name": "Rasel", "favourite_snack": "Burger"}, # here key is guest1 and value is right side all
    "guest2": {"name": "Ali", "favourite_snack": "Pizza"}
}
print(party_guest)

# Find something in instant time
print(party_guest['guest1']['favourite_snack'])

# Loop on nested dictionary
for guest_id, details in party_guest.items(): # items na dile keys and value eksathe pawa jabe na
    print(guest_id, "->", details['name'], "loves ", details['favourite_snack'])

