def inverted_right_angle_triangle(n):
    for row in range (n,0,-1):
        for col in range(row):
            print("*",end ="")
        print()

inverted_right_angle_triangle(6)