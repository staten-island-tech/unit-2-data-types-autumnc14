num=int(input("Please entr a number"))
num2=int(input("Please enter another number:"))
def gcf(x,y):
    for i in range(1, y):
        if x%i==0 and y%i==0:
            print(i)
#num and num2 should be x and y
gcf(num,num2)
#if you put 0 in "for i in range()", you are starting with 0. if you are diving by 0, you can't start with 0. 

