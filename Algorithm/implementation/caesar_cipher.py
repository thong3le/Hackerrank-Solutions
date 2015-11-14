def cipher(c, k):
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + k) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + k) % 26 + ord('A'))
    else:
        return c
    
n = input()
s = raw_input()
k = input()

print ''.join([cipher(c, k) for c in s])