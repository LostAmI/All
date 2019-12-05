
List = []

for i in range(1, 120):
    List.append(i+1)

fir = 2
sec = 3
thr = 5
fot = 7
print(fir, sec)
j = 0
while j != len(List):
    print(str(j) + ' = J')
    print(str(len(List)) + ' = Len')
    if List[j] != fir and List[j] % fir == 0:
        del List[j]
        print(str(List) + ' fir')
        j -= 1
    if List[j] != sec and List[j] % sec == 0:
        del List[j]
        print(str(List) + ' sec')
        j -= 1
    if List[j] != thr and List[j] % thr == 0:
        del List[j]
        print(str(List) + ' thr')
        j -= 1
    if List[j] != fot and List[j] % fot == 0:
        del List[j]
        print(str(List) + ' fot')
        j -= 1
    else:
        j += 1
        print('Shit')

# if List[j] % second == 0 and List[j] != second:
#     del List[j]
#     print(List)

