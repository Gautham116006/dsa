"""
Check if string is rotation or not

To check if two strings are rotations of each other, you can check if one string is a substring of the other string
concatenated with itself. If one string is a substring of the other string concatenated with itself, then the two
strings are rotations of each other.
"""

string_1 = 'abc'
string_2 = 'bac'


def rotation(s1, s2):
    s1 = s1 * 2
    if s2 in s1:
        return print(f'{s1[:len(s1)//2]}, {s2} are rotations of each other')
    else:
        return print(f'{s1}, {s2} are not rotations of each other')


rotation(string_1, string_2)
