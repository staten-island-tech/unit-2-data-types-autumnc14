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

#Factors and GCF 
num=int(input("Please enter a number"))
num2=int(input("Please enter another number:"))
factors = []
def gcf(x,y):
    for i in range(2, y):
        if x%i==0 and y%i==0:
            factors.append(i)
    print(max(factors))
    #save button = ctrl s 
#num and num2 should be x and y
gcf(num,num2)
























