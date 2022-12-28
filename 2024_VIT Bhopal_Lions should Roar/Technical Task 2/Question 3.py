"""Problem statement:-
Given an array, Arr[] of size T, contains binary digits where 
0 represents a biker running to the north.
1 represents a biker running to the south.
The task is to count crossing bikers in such a way that each pair of crossing bikers (N, S), where 0 <= N < S < T, is passing when N is running to the north and S is running to the South.

Example 1
Input
5
0
1
0
1
1

Output
5

Explanation
The 5 pairs are (Arr[0], Arr[1]), (Arr[0], Arr[3]), (Arr[0], Arr[4]), (Arr[2], Arr[3]) and (Arr[2], Arr[4])

Note
In all pairs the first element is 0, the second element is 1, and the index of the first element is smaller than the index of the second element.

Input format
The first line on input accepts a single positive integer value for T representing the size of an array
The second line of input accepts N number of integer values(0 or 1) separated by a new line.

Output format
The output must be a non-negative integer number.

Code constraints
0 <= N < S < T

Sample testcases
Input 1
5
0
1
0
1
1

Output 1
5

Input 2
4
1
0
1
0

Output 2
1

Code:-"""
"""Solution"""
array_size = int(input())
array = []
for i in range(array_size):
    array.append(int(input()))
    
crossing_bikers = 0
for i, element in enumerate(array):
    if element == 0:
        for j in range(i+1, array_size):
            if array[j] == 1:
                crossing_bikers += 1

print(crossing_bikers)
