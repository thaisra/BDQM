def print_reverse(number):
    if number <0 :
        raise ValueError("Please enter positive integer")
    reversed_number= str(number)[::-1]
    print(reversed_number)
print_reverse(6572)
S = [1, 15, 658, 2940, 44112]
for number in S:
    print_reverse(number)
