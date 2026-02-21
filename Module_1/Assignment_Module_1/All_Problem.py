# Problem 1
number = int(input("Enter Number: "))
if(number%2==0):
    print("Even Number")
else:
    print("Odd Number")    



# Problem 2
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operator = input("Enter operator(+,-,*,/): ")
print("Result is: ")
if operator=='+':
    print(num1+num2)
elif operator == '-':
    print(num1-num2)    
elif operator == '*':
    print(num1*num2)
elif operator == '/':
    print(num1/num2)    


# Problem 3
sum = 0
for i in range(1,101):
    if(i%2==0):
        sum = sum+i
print("Summation result: ",+sum)        