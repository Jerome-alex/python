def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    candidate = 2  # Start checking for primes from 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

# Get user input for the number of primes to generate
n = int(input("Enter the number of prime numbers to generate: "))
print(first_n_primes(n))

