"""
Find frequency of char's in a string and print them in sorted order. (all chars are lower-case)
"""

char_arr = [0] * 26

s = 'geeksforgeeks'

for char in s:
    char_arr[ord(char) - ord('a')] += 1

for char in range(26):
    if char_arr[char] > 0:
        print(f'{chr(ord("a")+char)} {char_arr[char]}')




