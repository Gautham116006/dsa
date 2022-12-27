"""
Check if given string is a palindrome or not
"""

ip = 'racecar'


def palindrome_checker(ip):
    i = 0
    j = len(ip) - 1
    while i < j:
        if ip[i] != ip[j]:
            return print('not palindrome')
        i += 1
        j -= 1
    return print('palindrome')


palindrome_checker(ip)
