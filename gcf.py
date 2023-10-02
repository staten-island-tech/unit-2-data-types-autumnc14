num=int(input("please enter a number"))
num2=int(input("please enter another number")) 
def gcf(x , y): 
    for i in range (1, y):
        if num%1==0 and num2%i==0:
            print(i)
gcf(x , y)


