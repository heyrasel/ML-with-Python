# For some mathematical calculation we have to import math 
import math

distance_to_home = 384400
gravity = 9.8
thrust_needed = math.sqrt(gravity * distance_to_home) # math.sqrt for root

print("Thrust needed: ",thrust_needed)






# Angle ber korbo
height = 15
base_length = 10

angle_radians = math.atan(height/base_length) #atan mane tan_inverse
print(angle_radians)
angle_degree = math.degrees(angle_radians) # radian theke degree te convert kore
print("Angle: ",angle_degree)
print("Angle: ",round(angle_degree)) #round mane decimal portion ta gayeb kore dibe
print("Angle: ",round(angle_degree,2)) # mane decimal er 2ghor nibe

print("Upper value: ",math.ceil(angle_degree)) # ceiling value ta nibe. deciamal value thaklei ceiling kore dibe
print("Lower value: ",math.floor(angle_degree))