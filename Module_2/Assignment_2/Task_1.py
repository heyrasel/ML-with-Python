# Task-1
list_task = input("Enter list elements: ").split()


def listConverter(list_task):
   original_list = list_task.copy()
   unique_list = list(dict.fromkeys(list_task))
   count_len = len(unique_list)

   result = {
      "Original list" : original_list,
      "Unique values" : unique_list,
      "Count" : count_len
   }
   return result

output = listConverter(list_task)
print(output)







