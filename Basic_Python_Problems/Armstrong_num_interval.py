start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    num_digit = len(str(num))
    temp_num = num
    sum_of_power = 0

    while temp_num > 0:
        digit = temp_num % 10
        sum_of_power += digit ** num_digit
        temp_num //=  10

    if sum_of_power == num:
        print(num)