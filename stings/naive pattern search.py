"""
Search for a pattern in a string given that all characters are distinct
"""

pattern = 'Geeks'
key = 'eks'


def pattern_search(p, k):
    head = 0
    while head <= len(p) - len(k):
        count = 0
        for i in range(len(k)):
            count += 1
            if k[i] != p[head + i]:
                break
        if count == len(k):
            return print('pattern found')
        head = count
    return print('no pattern found')


pattern_search(pattern, key)
