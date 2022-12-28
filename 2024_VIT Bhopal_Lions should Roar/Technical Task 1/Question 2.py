"""Problem statement:
Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. 

Sample Items: green-red-yellow-black-white
Expected Result: black-green-red-white-yellow

Input format
The input consists of a string separated by a hyphen.

Output format
The output prints the sorted string.

Sample testcases
Input 1
green-red-yellow-black-white

Output 1
black-green-red-white-yellow

Input 2
orange-mango-apple-water melon-grapes

Output 2
apple-grapes-mango-orange-water melon"""

"""Code:-"""
"""Solution 1:-"""
input_string = input()
words = input_string.split("-")
words.sort()
sorted_string = "-".join(words)
print(sorted_string)

"""Solution 2:-"""
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))
