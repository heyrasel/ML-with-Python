tupleA = (1,3.14,'abc')
integer_var, dub_var, string_var = tupleA
print(string_var)
tupleB = (1,5.3,9, 'rasel')

print(tupleA < tupleB)
print(tupleB < tupleA)
print(tupleA == tupleB)
print(tupleA != tupleB)




"""
The difference between list and tuples in python:
1. lists are mutable(changable)
2. tuples are immutable(we can't change it directly)
3. list uses []
4. tuples uses ()
5. tuples are generally faster ans safer for fixed data.
"""