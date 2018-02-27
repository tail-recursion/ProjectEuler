


'''
def factors(n):
    l = []
    for i in range(1,n+1):
        if n % i == 0:
            l.append(i)
    return l

def factors(n):
    return [i for i in range(1,n+1) if n % i == 0]
'''

def factors(n):

    def fac_helper(n, i, l=[]):
        if i == n:
            return l
        if n % i == 0:
            return fac_helper(n, i+1, l.append(i))
        else:
            return fac_helper(n, i+1, l)

    return fac_helper(n, i=1, l=[])


def prime_factorization(n):
    prime_factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            n = n / divisor
            prime_factors.append(divisor)
        divisor += 1
    return prime_factors

def least_common_multiple(a,b):
    pf_a = prime_factorization(a)
    pf_b = prime_factorization(b)
    pf_lcm = list(pf_b)
    for i in pf_a:
        if i in pf_b:
            pf_b.remove(i)
        else:
            pf_lcm.append(i)

    lcm = 1
    for i in pf_lcm:
        lcm *= i
    return lcm
