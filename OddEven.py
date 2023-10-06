#odd or even
BigQ= input ("TYPE  A NUMBER AND I WILL DETERMINE IF ITS EVEN OR ODD.") 
x = int(BigQ)
print(x) 
y = x % 2 
if y == 0:
        print("EVEN") 
elif y > 0: 
        print("ODD") 