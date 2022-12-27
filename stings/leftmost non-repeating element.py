"""
Find out left-most non-repeating character in a string. eg: in 'geeks for geeks' f is the left-most
non-repeating element
"""

string_1 = 'geeks for geeks'


def left_most_repeating(s1):
    char_arr = [0] * 26
    s1 = s1.replace(' ', '')

    for i in s1:
        char_arr[ord(i) - ord('a')] += 1

    for i in s1:
        if char_arr[ord(i) - ord('a')] == 1:
            return print(f'leftmost non repeating char: {i}')
    return print(f'all character repeating')


left_most_repeating(string_1)
