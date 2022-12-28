"""Problem statement:
Given two binary strings A and B.
Your task is to find how many cyclic permutations of B when taken XOR with A will give zero.

Input format
The first line contains A and the next line contains B.

Output format
The output consists of an integer

Code constraints
1 <= length(A) = length(B) <= 105

Sample testcases
Input 1
101
101

Output 1
1

Input 2
111
111

Output 2
3

Code:-"""
"""Solution:-"""
def count_zero_xors(a, b):
    count = 0
    for i in range(len(b)):
        permutation = b[i:] + b[:i]
        xor = int(a, 2) ^ int(permutation, 2)
        if xor == 0:
            count += 1
    return count
a = input()
b = input()
result = count_zero_xors(a, b)
print(result)
