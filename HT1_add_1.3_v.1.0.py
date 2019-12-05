import random

Number1 = random.randint(0, 1000)
Number2 = random.randint(1, 10)
print(Number1, Number2)

if Number1 % Number2 == 0:
    print('1')
else:
    print('NO!')