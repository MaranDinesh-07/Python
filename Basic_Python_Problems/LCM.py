"""Least Common Multiple (LCM):
LCM, or Least Common Multiple, is the smallest multiple that is exactly divisible by two or
more numbers.
Formula:
For two numbers a and b, the LCM can be found using the formula: LCM(𝑎, 𝑏) =|𝑎 ⋅ 𝑏| / GCD(𝑎, 𝑏)  For more than two numbers, you can find the LCM step by step, taking the LCM of pairs of
numbers at a time until you reach the last pair.
Note: GCD stands for Greatest Common Divisor."""
import math
a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
lcm = abs(a * b) // math.gcd(a,b)
print(f"The LCM is {lcm}")