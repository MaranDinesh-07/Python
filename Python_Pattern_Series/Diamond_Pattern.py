def diamondpattern(num):
# Upper part
 for row in range(1,num+1):
    for space in range(num - row):
        print(" ",end= "")
    for star in range(2*row -1):
        print("*",end= "")
    print()

# Lower Part
 for row in range(num-1,0,-1):
    for space in range(num - row):
        print(" ",end= "")
    for star in range(2*row - 1):
        print("*",end="")
    print()

diamondpattern(5)
