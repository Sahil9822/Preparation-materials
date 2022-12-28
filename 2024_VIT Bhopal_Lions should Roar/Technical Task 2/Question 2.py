"""Problem statement:
The numerological reduction of a number is the sum of digits calculated recursively until the resulting value is a single digit.
You are given a function,
int FindNumerologicalReduction(int n);
The function accepts a positive integer ‘n’. Implement the function to find and return the numerological reduction of ‘n’.

Assumption
n > 0

Example
Input
3245

Output
5

Explanation
3245 = 3 + 2 + 4 + 5 = 14
14 = 1 + 4 = 5
Hence 5 is the numerological reduction of 3245

Input format
Contains a single integer

Output format
The Sum of digits reduced up to single-digit

Sample testcases
Input 1
3245

Output 1
5

Input 2
12345

Output 2
6

Code:-"""
"""Soution 1:-"""
def Find(n):
    sum_of_digits = 0
    while n > 0:
        sum_of_digits += n % 10
        n //= 10
        
    if sum_of_digits < 10:
        return sum_of_digits
    else:
        return Find(sum_of_digits)
        
number = int(input())
print(Find(number))

"""Solution 2:-"""
def FindNumerologicalReduction(n):
    if (n == 0):
        return 0
    if (n % 9 == 0):
        return 9
    else:
       return (n % 9)
n = int(input())
print(FindNumerologicalReduction(n))
