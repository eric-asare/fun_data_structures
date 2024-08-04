""" 
Problem:
You're developing a new programming language with some unusual features for strings! Among these is a method that returns the longest palindrome that can be formed with the characters of a given string.

Given a string s, your task is to find this longest possible palindrome. You may use any number of the characters from s, and arrange them in any order (so long as it results in a palindrome).

If there are multiple longest palindromes that can be formed, return the one among them that's lexicographically smallest.

Examples :

For s = "aaabb", the output should be solution(s) = "ababa".

There are two possible palindromes of length 5 that can be obtained ("ababa" and "baaab"), but "ababa" is lexicographically smaller, thus it is the answer.

For s = "aaabbbcc", the output should be solution(s) = "abcacba".

It's not possible to form a palindrome of length 8, but from several palindromes of length 7, "abcacba" is the lexicographically smallest, thus it is the answer.
Other Examples:

Input:
s: "lollipop"
Expected Output: "lopipol"

Input:
s: "gfagcaabdfdgfaabeabbage"
Expected Output: "aaabbdefggaggfedbbaaa"
"""
 
s = "aaabbbcc"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

sorteds = sorted(set(s))

# form first half
firsthalf = []
for ch in s:
    if freq[ch] > 1:
        firsthalf.append(ch)
        freq[ch] -= 2

center = ''
# choose center, first ch with just 1 element
for ch in s:
    if freq[ch] > 0:
        center = ch
        break
        
palindrome = firsthalf + [center] + firsthalf[::-1]
print(''.join(palindrome)) #"abcacba"
         