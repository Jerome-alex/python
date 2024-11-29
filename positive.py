
user_input = input("Enter a list of integers separated by spaces: ")

numbers = [int(num) for num in user_input.split()]

positive_numbers = [num for num in numbers if num > 0]

print("Positive numbers:", positive_numbers)

