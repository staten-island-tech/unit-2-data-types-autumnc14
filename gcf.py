num=int(input("please enter a number:")) 
num2=int(input("please enter another number"))
def gcf():
    for i in range(0, -1):
        if num%i==0 and num2%i== 0:
            print(i)



