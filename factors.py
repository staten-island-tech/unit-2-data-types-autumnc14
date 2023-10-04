num=int(input("Please enter a number"))
num2=int(input("Please enter another number:"))
factors = []
def gcf(x,y):
    for i in range(2, y):
        if x%i==0 and y%i==0:
            factors.append(i) 
            print(max(factors)) 
#num and num2 should be x and y
gcf(num,num2)
#if you put 0 in "for i in range()", you are starting with 0. if you are diving by 0, you can't start with 0. 
#google append list python. When you append something, you are adding a new item to your existing list. 
