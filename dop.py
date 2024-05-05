import random

x = list(range(3, 20))
n = random.choice(x)
for i in range(n):
    for j in range(n):
        if ((n % (i + 1 + j + 1)) == 0) and (i + 1 != j + 1) and (i + 1 < j + 1):
            print(i + 1, end='')
            print(j + 1, end='')
