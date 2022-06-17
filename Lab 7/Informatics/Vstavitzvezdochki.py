s = input()
a = ''
for i in range(len(s)):
    if i + 1 != len(s):
        a += s[i:i + 1] + '*'
    else:
        a += s[i:i+1]
print(a)
