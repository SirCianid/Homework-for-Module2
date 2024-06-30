import random

n = random.randint(3, 20)
result = ''
for i in range(1, 21):
    for j in range(1, 21):
        if i != j and (i + j) % n == 0:
            result += str(i) + str(j)
print(n)
print(result)