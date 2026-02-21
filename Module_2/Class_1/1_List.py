# # Python e 4 dhoroner data type ache
# # 1. List, 2. Dictionary, 3. Set and 4.Tuple
# # Onekgula data list hisebe rakha jabe list use kore

# snacks = ["Cake", "Pepsi", "Pastry", "Soda"] # List evabe 3rd bracket er moddhe likhte hoy
# print(snacks)

# # Ekhn list e jodi kichu insert korte chai taile sheta list er last e add hobe
# snacks.append("Cookies")
# print(snacks)

# # For removing elements in list
# snacks.remove("Soda")
# print(snacks)

# # For alphabetacal order sorting
# snacks.sort()
# print("Sorted in alphabetical order: ",snacks)

# # Accessing elements
# print("First item: ",snacks[0])
# print("Last item: ",snacks[-1])

# # To find length
# print("Length of list: ",len(snacks))
# print("Last item: ",snacks[len(snacks)-1]) # -1 karon indexing 0 theeke start hoy always.

# # Kono index e value change korte
# snacks[3] = "Juice"
# print(snacks)

# # Kono index e kichu add korte
# snacks.insert(1,"Mango") # 1 number index e mango add korlam
# print(snacks)

# # Kono index er value delete korte
# del snacks[4] # 4 number index er value delete hoye jabe
# print(snacks)

# # For pop the last item
# last_item = snacks.pop()
# print("Last item which is poped: ",last_item)
# print("After poping: ",snacks)

# # For clearing list
# snacks.clear()
# print(snacks)






# Creating 2D list/ nested list
list_bags = [
    ["Cookies", "Pepsi"],
    ["Pastry", "Pizza"],
    ["Burger", "Juice"]
]

# Nested for-loop to iterate items
# for bag in list_bags:
#     for item in bag:
#         print(item)

index = 0
for bag in list_bags:
    index = index + 1
    if(index==2):
        break   # ekhane continue dile index=2 hole nicher for ta kaj korto na tokhon
    for item in bag:
        print(item)

