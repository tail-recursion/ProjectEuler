'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# compute prime factorization of all numbers from 1 to 20
# take minimal set that includes

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

facs = [] # prime factorization of numbers 1 to 20

for i in range(1,21):
    facs.append(prime_factors(i))

facs.sort(key=lambda x: len(x))

# want to generate minimal superset

min_superset = {}

for pf in facs:
    for i in pf:
        count = len([j for j in pf if j == i])
        if i in min_superset:
            min_superset[i] = max(min_superset[i], count)
        else:
            min_superset[i] = count

# min superset is the prime factorization of the answer
answer = 1
for key, value in min_superset.items():
    answer = answer * (key ** value)
print(answer)
