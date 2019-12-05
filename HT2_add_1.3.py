import random

# 3.2 HT2 add 3

# First figure(Horse)
x1 = random.randint(1, 8)
y1 = random.randint(1, 8)
print(x1, y1)

# Second figure(Ferz)
x2 = random.randint(1, 8)
y2 = random.randint(1, 8)
print(x2, y2)

# Option for gamex1 = int(input())
# (Horse vs Ferz)
if abs(x1 - x2) == 1 and abs(y1 - y2) == 2 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1: # for Horse
    print('Horse beet Ferz')

elif abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2: # for Ferz
    print('Ferz beet Horse')

else:
    print('The figures are safe')