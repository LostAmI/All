import random

# EX 1.1 v 1.4

# Rand or Inp option, to add same func

Quastion = input('Random or Input?')
if Quastion == 'Random' or 'random':
    SpendSec = random.randint(0, 86400)  # 1 Day
    print(str(SpendSec) + '\n')

elif Quastion == 'Input' or 'input':
    SpendSec = input('Enter time in seconds')
    print(str(SpendSec) + '\n')

# Time finder from clear obj(num).

Seconds = int(SpendSec % 60)
Minutes = int((SpendSec / 60) % 60)
Hours = int((SpendSec / 3600) % 24)
print('Seconds: ' + str(Seconds))
print('Minutes: ' + str(Minutes))
print('Hours: ' + str(Hours) + '\n')
print('Time:')

# Tree option skelet.

if Seconds < 10:
    if Minutes < 10:
        if Hours < 10:
            print('0' + str(Hours) + ':0' + str(Minutes) + ':0' + str(Seconds))
        else:
            print(str(Hours) + ':0' + str(Minutes) + ':0' + str(Seconds))
    else:
        if Hours < 10:
            print('0' + str(Hours) + ':' + str(Minutes) + ':0' + str(Seconds))
        else:
            print(str(Hours) + ':' + str(Minutes) + ':0' + str(Seconds))
else:
    if Minutes < 10:
        if Hours < 10:
            print('0' + str(Hours) + ':0' + str(Minutes) + ':' + str(Seconds))
        else:
            print(str(Hours) + ':0' + str(Minutes) + ':' + str(Seconds))
    else:
        if Hours < 10:
            print('0' + str(Hours) + ':' + str(Minutes) + ':' + str(Seconds))
        else:
            print(str(Hours) + ':' + str(Minutes) + ':' + str(Seconds))

### END ###
