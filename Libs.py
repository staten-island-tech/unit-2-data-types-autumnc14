#odd or even
BigQ= input ("TYPE  A NUMBER AND I WILL DETERMINE IF ITS EVEN OR ODD.") 
x = int(BigQ)
print(x) 
y = x % 2 
if y == 0:
        print("EVEN") 
elif y > 0: 
        print("ODD") 

#if x is true, and y is true = x and y ARENT equal
#if x is true + y is false =  x and y ARENT equal
#if x is false + y is True = x and y ARENT equal 
#if x is false + y is false = x and y are equal

y = True

def truthy (x,y):
        if x == y: 
                print ("False") 
        elif x != y:
                print ("true") 
truthy (x,y) 
#if you input a number instead of a word, itll keep showing true, thats a glitch. To look at 

#if type(x)!= bool or type (y) 


# if something is equal type (==), if it's not, then put (!=) 

