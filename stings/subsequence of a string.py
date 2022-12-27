"""
Check if a string is a  subsequence of another string (s2 subsequence of s1)
a subsequence is not a substring
"""

s1 = 'abcdefgh'
s2 = 'abcd'


def is_subsequence(s1, s2):
    shorter_index = 0
    for i in s1:
        if shorter_index == len(s2):
            return print('substring!')
        elif i == s2[shorter_index]:
            shorter_index += 1
    return print('not substring')


is_subsequence(s1, s2)
