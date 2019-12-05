import random

# 3.2 HT2 add 2

# First figure
x1 = random.randint(1, 8)
y1 = random.randint(1, 8)
print(x1, y1)

# Second figure
x2 = random.randint(1, 8)
y2 = random.randint(1, 8)
print(x2, y2)

delta_x = abs(x1 - x2)
delta_y = abs(y1 - y2)

# Option for game x1 = int(input())
# (Horse)

if delta_x == 1 and delta_y == 2 or delta_x == 2 and delta_y == 1:
    print('YES')
else:
    print('NO')