from random import randint

# HT2_Ex_1.1_v.1.0 lvl_1

count = set([i * (i % 3 == 0) for i in range(1, 100)])
print(str(count) + '\n')

# HT2_Ex_1.2_v.1.0 lvl_1

number1 = randint(20, 100)
countSum = [(i**2) for i in range(number1)]
print(str(countSum) + '\n')
print(str(sum(countSum)) + '\n')

# HT2_Ex_1.0_v.1.0 lvl_2

# Figure 1
x_1 = randint(1, 8)
y_1 = randint(1, 8)
print(x_1, y_1)

# Figure 2
x_2 = randint(1, 8)
y_2 = randint(1, 8)
print(x_2, y_2)

if x_1 == x_2 or y_1 == y_2:
    print("Yes!")
else:
    print("No!")

# HT2_Ex_1.0_v.1.0 lvl_3

a = randint(1, 100)
b = randint(1, 100)
c = randint(1, 100)
print(a, b, c)

max_ab = int((a + b + abs(a - b)) / 2)
print(max_ab)

if c > int(max_ab):
    print(c)
else:
    print(max_ab)