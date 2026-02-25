# class Avenger:
#     def fight(self): # class er under e kono function likhle parameter hisebe must be self likhtei hobe, karon ei method je ei class er seta bojhai.
#         print("Avengers is fighting!")




# # Creating object of the class
# ironman = Avenger() # ironman nam e ekta object create holo
# hulk = Avenger()
# ironman.fight() # ironman nam diye class er method ke access korte parbo
# hulk.fight()





# class Avenger:
#     def introduce(self, name): # parameter hisebe extra name o nicche
#         print(f"I am {name}, I can save the Regime:)")
    
#     def power(self, power):
#         print(f"I have {power} power")

# ironman = Avenger()
# spiderman = Avenger()
# ironman.introduce("Tony Stark")
# spiderman.introduce("Peter")
# spiderman.power("Web Shooting")







# Default constructor
# Constructor is used for intialize classes variable

# class Avenger:
#     def __init__(self): # evabe init likhte hoy constructor initialize korar jonno.
#         self.name = "Tony Stark" # self is like this keyword in java.
#         self.power = "Flying"
    
#     def introduce(self):
#         print(f"My name is: {self.name}")

#     def skill(self):
#         print(f"My skill is: {self.power}")

# ironman = Avenger()
# ironman.introduce() # ekhon ar name pass kora lagche na karon default hisebe to deyai ache
# ironman.skill()









# Parameterized constructor
# Constructor is used for intialize classes variable

class Avenger:
    def __init__(self,name, power):
        self.name = name
        self.power = power
    
    def introduce(self, mood):
        print(f"My name is: {self.name}, my mood is: {mood}") # mood er jonno self use kora lagbe na karon eta just ei method er parameter

    def skill(self):
        print(f"My skill is: {self.power}")

hulk = Avenger("Hulk","Stronger")
spiderman = Avenger("Peter Parker", 'Shooting Web')
hulk.introduce("Angry")
hulk.skill()
spiderman.introduce('Bad')