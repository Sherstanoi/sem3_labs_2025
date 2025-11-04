import math
def AreaCalculating(shapetype,a,b,c):
    # if(type(shapetype) == str and a>0 and b>=0 and c>=0):
        if(shapetype == "rectangle"):
            return a*b
        elif(shapetype == "square"):
            return a*a
        # elif(shapetype == "triangle"):
        #     per =(a+b+c)/2
        #     return int(math.sqrt((per*(per-a)*(per-b)*(per-c))))
    # else:
    #     return ValueError

print(AreaCalculating("triangle",3,4,5))
print(AreaCalculating("square", 3, 0, 0))
print(AreaCalculating("rectangle", 5, 12, 0))