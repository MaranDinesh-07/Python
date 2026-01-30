def rightangletriangleodd(num):
    for row in range(0, num ):
        for col in range(1,2*row):
            print("*",end= "")
        print()

rightangletriangleodd(7)