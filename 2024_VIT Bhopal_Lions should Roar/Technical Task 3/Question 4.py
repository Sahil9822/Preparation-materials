"""Problem statement:
Write a recursive function to calculate the power of a given number X raised to power y. (for example X y ). Accept X and y as inputs.

Input format
The input consists of the values of x and y.

Output format
The output consists of an integer

Sample testcases
Input 1
2
3

Output 1
8

Input 2
4
4

Output 2
256

Code:-"""
"""Solution 1:-"""
x = int(input())
y = int(input())
print(x**y)

"""Solution 2:-"""
def power(x, y):

	if (y == 0): return 1
	elif (int(y % 2) == 0):
		return (power(x, int(y / 2)) *
			power(x, int(y / 2)))
	else:
		return (x * power(x, int(y / 2)) *
				power(x, int(y / 2)))

x = int(input())
y = int(input())
print(power(x, y))
