"""Problem statement
In the game of scrabble, in order to avoid over-usage of the same letters in any word. Mario is trying to calculate if a letter appears more than three times in any word and wants to discard such words. In order to assist Mario, write a program to identify the number of times the most repeating letter would appear within any word. If the output number is more than three, Mario shall discard such words and choose another word for the game.

Example 1
Input
trumpet

Output
2 -> Highest number of repeating letters in the word trumpet.

Explanation
The word "trumpet" has 2 occurrences of the letter 't'; the rest of the letters appear only once.

Example 2
Input
reiterate

Output
3 -> Highest number of repeating letters in the word reiterate.

Explanation
The word "reiterate" has 3 occurrences of the letter 'e', the rest of the letters appear only once or twice.
Hence the output is 3.

Input format
The input accepts a single-string value (lowercase alphabet).

Output format
The output should be a positive integer number.

Code constraints
str = {a-z}

Sample testcases
Input 1
trumpet

Output 1
2

Input 2
reiterare

Output 2
3

Code:-"""
"""Solution"""
word = input()
letter_counts = {}
for letter in word:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1
        
most_common_letter = max(letter_counts, key = letter_counts.get)
print(letter_counts[most_common_letter])
