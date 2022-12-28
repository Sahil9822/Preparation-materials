"""Problem statement:
Write a program to check whether the given matrix is square or not.

Input format
The first line of the input consists of the number of rows and columns.
The next input is the matrix.

Output format
The output prints the matrix.
Then whether the matrix is square or not.

Refer sample output.
Sample testcases
Input 1
3 3
1 2 3
4 5 6
7 8 9

Output 1
1 2 3 
4 5 6 
7 8 9 
The entered array is a square matrix.

Input 2
3 4
1 2 3 4
5 6 7 8
9 10 11 12

Output 2
1 2 3 4 
5 6 7 8 
9 10 11 12 
The entered array is not a square matrix.

Code:-"""

num_rows, num_cols = map(int, input().split())
matrix = []
for i in range(num_rows):
    matrix.append(list(map(int,input().split())))
for row in matrix:
    print(*row)
if num_rows == num_cols:
    print("The entered array is a square matrix.")
else:
    print("The entered array is not a square matrix.")
