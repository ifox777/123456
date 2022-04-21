s = input()
counter = 0
for i in range(0, len(s)):
    if s[i] == s[i - 1]:
        counter += 1

print(counter)
#11111111111111111111111111111111111111
