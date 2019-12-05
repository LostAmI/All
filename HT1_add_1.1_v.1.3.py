import random

# EX 1.1 v 1.3

SpendMin = random.randint(0, 8760)
print(str(SpendMin) + '\n')

Minutes = SpendMin % 60
Hours = SpendMin % 24
print('Minutes: ' + str(Minutes))
print('Hours: ' + str(Hours) + '\n')
print('Time:')

if Minutes < 10:
    print(str(Hours) + ':0' + str(Minutes))
    if Hours < 10:
        print('0' + str(Hours) + ':0' + str(Minutes))

elif Minutes >= 10 and Hours < 10:
    print('0' + str(Hours) + ':' + str(Minutes))
else:
    print(str(Hours) + ':' + str(Minutes))

### END ###