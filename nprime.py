from math import sqrt

n = int(input("Enter the range: "))
count = 0
num = 2

print("First", n, "prime numbers:")

while count < n:
    is_prime = True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
            
    if is_prime:  # Move this outside the for loop
        print(num, end=" ")
        count += 1
        
    num += 1

