"""Problem statement:
An English school teacher is teaching how to build sentences for kindergarten students. She starts by teaching two words in a sentence, then 3 words, and so on. The next step is that she asks the students to find which word in the sentence they have made has the maximum value of the alphabet. The task here is to write a program to find the longest word in each input sentence(str)

Note
The sentence can consist of uppercase, lowercase alphabets, special characters, and numbers.

Example 1
Input
Knowledge is the greatest gift

Output
9

Explanation
Word No. of characters
Knowledge 9
is 2
the 3
greatest 8

Input format
The input consists of a string

Output format
The output prints an integer denoting the length of the longest word.

Sample testcases
Input 1
Knowledge is the greatest gift

Output 1
9

Input 2
Length of the longest word

Output 2
7

Code:-"""
"""Solution:-"""
def find_longest_word(sentence):
    words = sentence.split()
    longest_word = words[0]
    longest_word_length = len(longest_word)
    for word in words[1:]:
        if len(word) > longest_word_length:
            longest_word = word
            longest_word_length = len(word)
    return longest_word_length
sentence = input()
result = find_longest_word(sentence)
print(result)
