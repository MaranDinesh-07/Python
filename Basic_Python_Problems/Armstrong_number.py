num = int(input("Enter a number:"))
num_digit= len(str(num))

sum_of_power= 0
temp_num = num

while temp_num > 0:
    digit= temp_num % 10
    sum_of_power += digit ** num_digit
    temp_num //= 10

if sum_of_power == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

