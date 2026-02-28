# # Single Inheritance

# class Father:
#     def skills(self):
#         print("I can code with C++")


# class Son(Father): # Mane Son class Father class ke inherit korlo
#     pass # let son er ekhn onno kichu nai

# inno = Father() # let inno holo son er nam
# inno.skills()  # As son father class ke inherit koreche so father er skill method sun er skill method hoye jabe








# Multiple Inheritance

# class Mom:
#     def skills(self):
#         print("I can cook delicious biriyani")

        
# class Boy(Mom): # boy inherits mom
#     pass

# class Girl(Mom): # girl inherits mom
#     pass

# boy = Mom() # boy inherits mom
# boy.skills() # as boy inherits mom so mom class er skill boy class e chole ashbe.
# girl = Mom()
# girl.skills()







# # Multi-level Inheritance

# class Grandpa:
#     def advice(self):
#         print("I can provide life-lesson")

# class Father(Grandpa): # Father inherits Grandpa so Father er kache by default Grandpa er method o thakbe
#     def teach(self):
#         print("I can teach code.")

# class Son(Father): # As Father inherits Grandpa and Son inherits Father so Son er kache Grandpa and Father 2joner e method gula thakbe
#     pass

# son = Son()
# son.advice() # son er kache advice and teach 2ta method e thakbe
# son.teach()

# father = Father()
# father.teach()
# father.advice()









# # Multiple Inheritance
# class Mom:
#     def dicipline(self):
#         print("Go to bed at 10AM!")

# class Nani:
#     def skill(self):
#         print("I have very good cooking skills")

# class Daughter(Mom,Nani): # Mom and Nani 2joner method e pabe Daughter.
#     pass

# daughter = Daughter()
# daughter.dicipline()
# daughter.skill()








# Method overloading
# Method name same but parameter is different
# Java and python e method overloading alada.

# class ReportCard:
#     def marks(slef, math=None, english = None): # jodi math and english er value na diy taile by default None dhore nibe
#         if math is not None and english is not None: # jodi math and english exam dei taile 2tar marks e print korchi
#             print(f"Math: {math}, English: {english}")
#         elif math is not None: # jodi math exam ta dei only
#             print(f"Math: {math}")
#         elif english is not None: # jodi english exam ta dei only
#             print(f"English: {english}")
#         else:
#             print("No exam is given!")

# rpCard = ReportCard()
# rpCard.marks(None,14) # method overloading karon different different parameter pass korte parchi
# rpCard.marks(90,95)










# Method Overriding
class Parent:
    def role(self):
        print("We are parent and we do everything!")

class Chlid(Parent): # Child class inherits Parent class
    def role(self): # as both child and parent class same method name so this is method overriding
        print("Now we are child and we control everything now!")


child = Chlid()
child.role() # ekhon child er role ta output e ashbe karon child class role method ke override koreche.
