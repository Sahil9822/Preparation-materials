"""Problem statement:
7 types of Indian currency notes are given, ie, Re. 1, Rs. 2. Rs. 5, Rs10, Rs 20, Rs 50, and Rs 100.
You are required to implement the following function
int MinNumberOfNotes (int n);
The function accepts an integer 'n' as its argument. Implement the function to find and return the minimum number of notes required to form the amount 'n'.

Assumption
n>=0

Note
Return 0, if n=0
multiple notes of the same type can be used

Input format
The input consists of an integer

Output format
The output consists of an integer

Sample testcases
Input 1
175

Output 1
4

Input 2
84

Output 2
5

Code:-"""
"""Solution:-"""
def min_number_of_notes(n):
    notes = [100, 50, 20, 10, 5, 2, 1]
    count = 0
    for note in notes:
        while n >= note:
            count += 1
            n -= note
    return count
n = int(input())
result = min_number_of_notes(n)
print(result)
