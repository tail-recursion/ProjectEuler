'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

def prime_factors(n):
    # returns prime factorization of n
    d = 2
    factors = []
    while n > 1:
        while n % d == 0:
            n = n / d
            factors.append(d)
        d = d + 1
    return factors

largest = max(prime_factors(600851475143))

print(largest)
