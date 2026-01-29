for x in range(1,21):
    insteadOf = False
    if(x%3==0):
        print("Fizz",end="")
        insteadOf = True
    if(x%5==0):
        print("Buzz",end="")
        insteadOf = True
    if( not insteadOf):
        print(x,end="")


    print("")