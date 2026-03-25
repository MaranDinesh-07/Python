# Write a Python program to swap two variables without temp variable.
a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
print("Before Swapping")
print("a =",a)
print("b =",b)
# Swapping without temporary variable
a,b = b,a
print("After Swapping:")
print("a =",a)
print("b =",b)