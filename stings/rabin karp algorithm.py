"""
Pattern search using Rabin-Karp algorithm
"""

alphabet_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'r': 8, 'y': 9}


def hash_func(pattern):
    result = 0
    for i in range(len(pattern)):
        result += alphabet_map[pattern[i]] * 10 ** (len(pattern) - i - 1)

    return result


def pattern_search(text, pattern):
    start = 0
    end = len(pattern)
    pattern_hash = hash_func(pattern)
    text_hash = hash_func(text[:end])

    if pattern_hash == text_hash:
        return start
    for i in range(end, len(text)):
        text_hash = 10 * (text_hash - alphabet_map[text[start]] * 10 ** (len(pattern) - 1)) + alphabet_map[text[end]]
        if text_hash == pattern_hash:
            return f'{text[:start]}"{text[start + 1:end + 1].upper()}"{text[end:]}'
        start += 1
        end += 1
    return 'Pattern not found in text'


print(pattern_search('abcdefabcdeffedabccefdabbccaaagracyaaeefbcaedaabbeeffaceebaaaabcccef', 'gracy'))
