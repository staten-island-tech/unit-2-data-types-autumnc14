def highestFactor(numX,numY):
    if numX > numY:
        x = numY
    else:
        x = numX
    while x > 1: 
#"while loops" -  A while loop ends if and only if the condition is true. 
#if x (numX or NumY) is greater than 1, 
        if numX % x == 0 and numY % x == 0:
            break
        x =- 1
    #x-=1 means to 
    print (x)
highestFactor(8,22)




