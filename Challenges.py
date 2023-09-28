#Tip Calculator
service= input ("tip value")
if service== "bad":
        print("0%") 
elif service== "okay":
        print("15%") 
elif service== "good":
        print("20%")
elif service== "great":
        print("25%")


#odd or even
BigQ= input ("TYPE  A NUMBER AND I WILL DETERMINE IF ITS EVEN OR ODD.") 
x = int(BigQ)
print(x) 
y = x % 2 
if y == 0:
        print("EVEN") 
elif y > 0: 
        print("ODD") 

# All factors of the number
def the_factors(x):
        print("these are the factors of x:") 
        for i in range (1, x+1): 
                if x % 1 == 0 : 
                        print(i) 
the_factors(100)

























