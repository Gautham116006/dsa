"""
Check if string is an anagram or not
"""

string_1 = 'Car'
string_2 = 'arc'


def anagram_checker(s1, s2):
    if len(s1) != len(s2):
        return print(f'Not anagram')

    s1 = s1.strip().lower()
    s2 = s2.strip().lower()
    char_arr = [0] * 26

    for i in s1:
        char_arr[ord(i) - ord('a')] += 1
    for i in s2:
        char_arr[ord(i) - ord('a')] -= 1
    for i in char_arr:
        if i != 0:
            return print(f'Not anagram')
    return print(f'Anagram')


anagram_checker(string_1, string_2)
