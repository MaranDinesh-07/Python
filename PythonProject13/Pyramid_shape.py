def pyramidpattern(num):
    for row in range (1,num+1):
        for space in range(num-row):
            print(" ",end="")
        for star in range (row):
            print("*",end=" ")
        print()

pyramidpattern(5)
