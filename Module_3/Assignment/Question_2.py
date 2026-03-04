class Animal:
    def eat(self):
        print("Animal Eats.")

class Mammal(Animal):
    def walk(self):
        print("Mammal can walk")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.eat()
dog.walk()
dog.bark()



class Calculator:
    def add(self,a,b):
        print("From add method: ",a+b)

class AdvancedCalculator(Calculator):
    def add(self,*args):
        sum = 0
        for i in args:
            sum = sum + i
        print(f"Sum: {sum}")
    

calc = Calculator()
calc.add(20,40)
advcalc = AdvancedCalculator()
advcalc.add(10,20)
advcalc.add(103,42,53,89)
advcalc.add(5,3,8,2,1,7)
