'''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?

'''


'''
    the smallest factor of any number, besides 1, is 2
    the largest possible factor of any number corresponds to this 2

    the largest possible factor of any number is half that number

    but we only need to try numbers from 2 to sqrt(n)
'''
import math

def is_prime(n):
    '''
    Simplest way to tell if a number is prime is iterate through all the numbers from 2 to n-1 and check if n is divisble by i
    But the largest possible factor of a number is half that number, so we only need to iterate from 2 to n/2
    But this is still doing some extra work:
    Each of the factors larger than sqrt(n)
    corresponds to another factor less than sqrt(n)
    e.g. 2 corresponds to n/2
    we only need to check one of these factors, not both
    therefore we only need to iterate from 2 to sqrt(n)
    '''
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    '''
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    '''
    return True


count = 0
i=2
while count < 10001:

    if is_prime(i):
        count += 1

    i += 1

print(i-1)
