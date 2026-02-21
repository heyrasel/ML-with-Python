# Task-2
def setTask(set1 = {'a','b', 'c'}, set2 = {'1','2','x', 'a', 'z'}):
   set3 = set1.union(set2)
   set4 = set1.intersection(set2)
   set5 = set1.difference(set2)
   return set3, set4, set5 # returning as like tuple values


set1 = {'apple', 'banana', 'orange', 'dates', 'apple'}
set2 = {'apple', 'watermelon', 'mango', 'jackfruit'}
# to receive the values we can unpack the tuple values
union_value, intersection_value, difference_value = setTask(set1,set2) # if we do not pass the values then default argument value will be used.
print(union_value)
print(intersection_value)
print(difference_value)