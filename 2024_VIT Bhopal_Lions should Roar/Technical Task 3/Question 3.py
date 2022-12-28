"""Problem statement:
Sum of numbers with a set bit
You are given a function,
int SumofSetBitNumbers(int n, int set);
The function accepts two integers ‘n’ and ‘set’ as its argument where ‘n’ is the number of bits and ‘set’ is the number of set bits. Implement the function to find the sum of all numbers possible from ‘n’ bits having the count of ‘set’ bits equal to set.

Note
n > 0
set >= 0

Example
Input
n: 3
set: 2

Output
14

Explanation
All possible 3-bit numbers are 0, 1, 2, 3, 4, 5, 6, and 7 with binary representations 000, 001, 010, 011, 100, 101, 110, 111. Numbers with 2 bits set are 3, 5, and 6 summation of which is equal to 14.

Input format
The first line of integer input represents the number of bits
The second line of integer input represents the number of set bits in the binary representation.

Output format
Sum of all possible decimal values of n bits with the exact number of set bits.

Sample testcases
Input 1
3
2

Output 1
14

Input 2
2
1

Output 2
3

Code:-"""
"""Solution:-"""
def sumofSetBits(n, setbit):
    sum = 0
    r = 2**n
    for i in range(0, r):
        count = 0
        m = i
        while(m != 0):
            m = m & (m - 1)
            count = count + 1
        if (count == setbit):
            sum = sum + i
    return sum
n = int(input())
setbit = int(input())
print(sumofSetBits(n, setbit))
