# a = [1, 1, 2, 3, 3, 3, 4, 4, 1, 5, 5, 4, 3, 2, 1, 0]
# count = [0] * 6
# for i in a:
#     count[i] += 1
# print(count)
# for i in range(6):
#     if count[i] > 0:
#         print(i, count[i], end=', (')
#         print((str(i) + '') * count[i], end='). ')

s = 'hagqtWAEQZXSWfevdabcnmz,.xlkdiorpitnght hfndjl;a]/.x,mcnbbhq'
for i in s.lower():
    if i >= 'a' and i <= 'z':
        print(i, ord(i))
        for n in range(i):

