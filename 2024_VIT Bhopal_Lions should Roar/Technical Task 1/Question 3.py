"""Problem statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23. Write a program to find the sum of all the multiples of 3 or 5 below n (Including n).

Input format
The input consists of an integer

Output format
The output prints the sum of all the multiples of 3 and 5 including n.

Sample testcases
Input 1
500

Output 1
58418

Input 2
1000

Output 2
234168

Code:-"""
"""Solution 1:-"""
n = int(input())
sum = 0
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)

"""Solution 2:-"""
sum=0 
n = int(input())
for num in range(1,n+1): 
    if num%3==0 or num%5==0: 
        sum=sum+num 
print(sum) 
