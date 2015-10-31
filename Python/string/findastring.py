s = raw_input()
word = raw_input()

k = len(word)
count = 0
for i in range(len(s)):
    if s[i:(i+k)] == word:
        count += 1
print count 