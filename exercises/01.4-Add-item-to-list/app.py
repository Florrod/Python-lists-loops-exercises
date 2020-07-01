#Remember import random function here:
import random

my_list = [4,5,734,43,45]

for i in range(0,10): # utilizamos un loop para repetir algo 10 veces en esta ocasión no para recorrer el array
    my_list.append(random.randint(0,1000))

print(my_list)

#The magic is here:
