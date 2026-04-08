"""How can we manually convert a decimal number to binary, octal and hexadecimal?
Converting a decimal number to binary, octal, and hexadecimal involves dividing the
decimal number by the base repeatedly and noting the remainders at each step. Here's a
simple example:
Let's convert the decimal number 27 to binary, octal, and hexadecimal.
1. Binary:
Divide 27 by 2. Quotient is 13, remainder is 1. Note the remainder.
Divide 13 by 2. Quotient is 6, remainder is 1. Note the remainder.
Divide 6 by 2. Quotient is 3, remainder is 0. Note the remainder.
Divide 3 by 2. Quotient is 1, remainder is 1. Note the remainder.
Reading the remainders from bottom to top, the binary representation of 27 is 11011.
2. Octal:
Divide 27 by 8. Quotient is 3, remainder is 3. Note the remainder.
Divide 3 by 8. Quotient is 0, remainder is 3. Note the remainder.
Reading the remainders from bottom to top, the octal representation of 27 is 33.
3. Hexadecimal:
Divide 27 by 16. Quotient is 1, remainder is 11 (B in hexadecimal). Note the
remainder.
Reading the remainders, the hexadecimal representation of 27 is 1B.
So, in summary:
Binary: 27 in decimal is 11011 in binary.
Octal: 27 in decimal is 33 in octal.
Hexadecimal: 27 in decimal is 1B in hexadecimal."""

d_num = int(input("Enter a decimal number: "))
print(f"The decimal value of {d_num} is:")
print(bin(d_num),"in Binary.")
print(oct(d_num),"in Octal.")
print(hex(d_num),"in Hexadecimal.")