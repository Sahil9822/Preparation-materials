"""Write a function to check whether a number is perfect or not. In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).

Example: The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

Input format
The input consists of a number.

Output format
The output prints whether the number is perfect or not.

Refer sample input and output for formatting specifications.

Sample testcases
Input 1
6

Output 1
6 is a perfect number

Input 2
100

Output 2
100 is not a perfect number
Code:-"""
"""Soultion 1:-"""
def is_perfect(n):
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
            
    if divisor_sum == n:
        return f"{n} is a perfect number"
    else:
        return f"{n} is not a perfect number"

number = int(input())
print(is_perfect(number))

"""Solution 2:-"""
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
    
num = int(input())
res = perfect_number(num)
if res == True:
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")
