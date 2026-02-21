# this_sets = {"apple", "orange", "banana",1, True,2,3} # Age true thakle 1 ta ar print korto na tokhon
# print(this_sets)

# # To add in set
# this_sets.add("Hello")
# print(this_sets)





# # Ekta set er moddhe arekta set er value add korte hole
# this_sets_two = {"ABC", "XYZ", "PQR","SRT"}
# this_sets.update(this_sets_two)
# print(this_sets)




# # List er jinish o set e add kora jabe
# list_example = ["Kiwi", "apple", "jackfruit"]
# this_sets_two.update(list_example)
# print(this_sets_two)





# # For removing elements from set
# this_sets_two.remove("Kiwi")
# print(this_sets_two)

# # Another way
# this_sets_two.discard("apple")
# print(this_sets_two)





# # For pop elements: set e pop korle random jekono value set theke ashe. list er moto last element ta ase na
# x = this_sets_two.pop()
# print(x)






# Set diye union,intersection, difference kora jai.
# Union mane sobgula gula nibe
# Intersection mane only common gula nibe

set_1 = {"a","b","c", 'rasel'}
set_2 = {"x", 'y', 'z', 'rasel'}
set_3 = set_1.union(set_2) # union korle 2 set er sobgula value pabo but duplicate value thakle 1ta dibe output e.
print(set_3)

set_4 = set_1.intersection(set_2) # 2ta set er moddhe common value ta pabo just.
print(set_4)


# difference kora mane biyog kora.
# set_1 - set_2 korle set1 and set2 te jeta common seta set1 theke bad hoye set1 er result ta dekhabe
# set_2 - set_1 korle set1 and set2 te jeta common seta set2 theke bad hoye set2 er result ta dekhabe

set_5 = set_1.difference(set_2)
print(set_5)

set_6 = set_2.difference(set_1)
print(set_6)
