# # String slicing
# tweet = "Hello Earth, rasel is here reporting sector 9"

# print("Start tweet from ",tweet[0:5]) # python e 0:5 mane 5 er ag porjonto dekhabe
# print("Start tweet from ",tweet[:5]) # python automatic 0 theke indexing kore so 0 na dileo hobe jodi 0 theke start hoy

# # Jodi last er dik theke slicing korte chai: python e last er diker indexing start hoy -1 theke
# print("From end: ",tweet[-7:]) # mane -7 index theke last porjonto
# # Majher kono string print korte
# print("Middle of tweet: ",tweet[26:37]) # mane 26 theke 37 porjonto
# # length of tweet
# print(len(tweet))





# # lets messy kichu likhe felche
# messy = "Visit####! earth!! its soo##o gree##n"
# cleaned_text = messy.replace('#', "").replace("!","") # mane # ke empty diye replace korlam. then abar ! ke empty diye replace korlam
# print(cleaned_text)
# print(cleaned_text.upper()) # mane cleaned text take sob boro hate dekhabe
# print(cleaned_text.lower())
# print(cleaned_text.capitalize()) # mane starting letter ta boro hater hobe





# planet = "Earth"
# temperature = 26.54
# weather = 'Mild' # double and single qutation string e mean kore same

# report = "Planet: "+planet+ ", Tempereture: "+str(temperature)+ ", Weather: "+weather
# print(report)

# # Another style to print
# report = "Planet: {}, Temp: {}, Weather: {}".format(planet,temperature,weather)
# print(report)

# # Another style to print
# report = f"Planet: {planet}, Temp: {temperature}, Weather: {weather}"
# print(report)

# mass = 75.534453
# print(f"Mass: {mass: .2f}")





# Spiliting text
text = "My name is Rasel"
words = text.split("is") # is diye split hobe
print(words)