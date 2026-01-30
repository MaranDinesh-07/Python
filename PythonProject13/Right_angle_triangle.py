def rightangletriangle(num):
    for row in range (0, num):
        for col in range(0,row+1):
            print("*",end ="")
        print()

rightangletriangle(6)