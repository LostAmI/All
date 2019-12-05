import random

#1
print("\nEx 1 for nums\n")
num = print((int(4 * '175') ** 10) ** (1 / 10))

#2
print("\nEx 2 for str\n")
string = 'Волка кормят ноги, а меня женщины из буфета'
print(string.count('e'), len(string), string.upper())

#3
print("\nEx 3 for nums\n")
print(int('175' * 50) ** 2)

#4
print("\nEx 4 for str\n")
s = "i wish i were special"
s1 = 'were'
s2 = 'was'
print(s.replace(s1, s2))

#5
print("\nEx 5 for str\n")
Original = '123456789876543212345'
print(Original[-1])

#6
print("\nEx 6 for nums\n")
long = 109
strtpoint = 0
v = random.randint(-1000, 1000)
t = random.randint(-1000, 1000)
print(v, t)
Sf = (v*t) % long
print(Sf)