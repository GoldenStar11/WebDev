x = int(input())
c = 0
for i in range(1, x + 1):
    if x % i == 0:
        c += 1
print(c)
