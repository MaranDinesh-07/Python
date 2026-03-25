# Write a Python program to swap two variables
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")
print(f"Original Values : a = {a}, b = {b}")
# Swap
temp = a
a = b
b = temp
print(f"Swapped values: a = {a} , b = {b}")