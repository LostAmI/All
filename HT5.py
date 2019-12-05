from functools import reduce
from random import randint

s = "Было просто пасмурно, дуло с севера \
А к обеду насчитал сто градаций серого. \
Так всегда первого ноль девятого \
То ли весь мир сошёл с ума, то ли я - того... \
На столе записка от неё смятая \
Недопитый виски допиваю с матами. \
Посмотрю в окно, допишу главу \
Первое сентября, дворник жжёт листву. \
Серым облакам наплевать на нас \
Если знаешь как жить - живи \
Ты хотела плыть как все - так плыви!"

# lvl_1_v_1.0
Spisok = s.split()
Filt = list(filter(lambda x: len(x) > 5, Spisok))
print(Spisok)
print(Filt)

f = open("1.txt", "w")
for i in range(len(Filt)):
    f.write(str(Filt[i]) + '\n')
f.close()

# lvl_2_v_1.0

f1 = open('1.txt','r')
print(f1.read()) # for x in f1:
                    # print(x)

# lvl_3_v_1.0

N = randint(1, 9)
print(N)
L = []*N
for i in range(len(L)):