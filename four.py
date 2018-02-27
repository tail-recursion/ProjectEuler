'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(s):
    even = len(s) % 2 == 0
    end  = len(s) // 2
    if even: end += 1
    for i in range(0, end):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def largest_palindrome():
    products = sorted([x*y for x in range(999,850,-1) for y in range(999,850,-1)], reverse=True)
    for i in products:
        if is_palindrome(str(i)):
            print(i)
            return
