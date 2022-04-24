import math            #First import math modules to use sine and cosine functions

i = 0
while i <= 345:        #While loop is used to make a loop of each 15degree angles
    sine = math.sin(math.radians(i))    #using sine and cosine functions from math module
    cosine = math.cos(math.radians(i))
    
    print(i,"---", round(sine, 4),",",i, round(cosine, 4))
    i+= 15
