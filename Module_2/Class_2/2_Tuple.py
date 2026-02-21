
# myTuple = ("apple", "banana", "orange","cherry", "cherry","dates") # duplicate value allow here.
# print(myTuple)
# print(len(myTuple))

# # Tuple e and list indexing maintain kore. just set and dictionary te indexing maintain kore na.
# print(myTuple[2])
# print(myTuple[-1]) # for last element

# # tuple e slicing o kora jai list er moto
# print(myTuple[2:5]) # mane 2 theke 4 porjonto output e pabo.






# Tuple ke directly modify kora jai na but process er maddhome kora jai
# tuple e element add remove, change etc korte hole tuple ke first e list e convert korte hobe then oi list ke modify korte hobe. 
# then oi list abar tuple e convert korte hobe.

# tupleA = ("dates", 'jackfruit', 'mango', 'litchi')
# # let ekhn jackfruit ke apple diye replace korbo, so ekhn ei tuple ke list e convert korte hobe
# listA = list(tupleA)
# print(listA)

# listA[1] = 'apple'
# print(listA)

# # ekhn abar listA ke tuple e convert korbo
# tupleA = tuple(listA)
# print(tupleA)

# # Evabe list e ja ja kora jaito tuple eo same jinish kora jabe evabe convert kore.








# Tuple ke unpack kora jai mane tuple er value gula kono varaiable e rakha jai

fruits = ('apple', 'banana', 'orange', 'strawberry', 'raspberry')
# ekhn let 3 ta variable e ei 5ta data rakhbo but 3ta variable e to 5ta data rakha jai na ejonne:
(green, yellow, *red) = fruits   # Mane apple ta jabe green variable e, banana ta jabe yellow variable e and bakigula sob jabe red variable e. * jetate deya thakbe setai remaining gula jabe. but 2ta * diye rakha jai na. only one * hobe
print(green)
print(yellow)
print(red)
