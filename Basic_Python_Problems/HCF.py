"""Highest Common Factor(HCF):
HCF, or Highest Common Factor, is the largest positive integer that divides two or more
numbers without leaving a remainder.
Formula:
         For two numbers a and b, the HCF can be found using the formula: HCF(𝑎, 𝑏) = GCD(𝑎, 𝑏)
For more than two numbers, you can find the HCF by taking the GCD of pairs of numbers at
a time until you reach the last pair.
Note: GCD stands for Greatest Common Divisor.
"""
import math
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
hcf = (math.gcd(a,b))
print(f"The HCF is {hcf}")