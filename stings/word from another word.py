"""
Check if a word can be formed from the letters of another word i.e. string_2 from string_1
"""
string_1 = 'Gracy sundar'
string_2 = 'gracy'


def make_new_word(s1, s2):
    d1 = {}
    for i in s1.lower():
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
    for i in s2.lower():
        if i not in d1:
            return print(f'Cannot form {s2} from {s1}')
        else:
            d1[i] -= 1

    for i in d1.values():
        if i < 0:
            return print(f'Cannot form {s2} from {s1}')

    return print(f'Can form {s2} from {s1}')


make_new_word(string_1, string_2)
