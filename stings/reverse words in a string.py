"""
Reverse the words in a string eg: welcome to gfg -> gfg to welcome

algorithm: reverse each word ina string and reverse the entire string
"""

string_1 = 'welcome to gfg'


def reverse_words(s1):
    i, j = 0, 0
    while j < len(s1):
        if s1[j] == ' ':
            reverse(i, j, s1)
            i = j + 1
        j += 1
    reverse(i, j, s1)
    reverse(0, len(s1) - 1, s1)
    return print(f'reversed: {s1}')


def reverse(i, j, s1):
    pass


reverse_words(string_1)
