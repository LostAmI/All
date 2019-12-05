import random

# HT_1.1 v 1.0

# List_Distance = int(input('Count of numbers in list'))
# List_range_min = int(input('Count of min list range'))
# List_range_max = int(input('Count of max list range'))
#
# def Generation_v_1(List_Distance, List_range_min, List_range_max):
#     return [random.randint(List_range_min, List_range_max) for Count in range(List_Distance)]
#
#
# print(Generation_v_1(List_Distance))

# HT_1.2 v 1.0

words = "Мне больше нравится слушать как ты молчишь, только за этим я тебя и зову гулять"

def upgrade(words):
    Change_list = words.split()
    list_for_changes = []
    print(Change_list)
    print(list(range(len(Change_list))))
    for i in range(len(Change_list)):
        if (i+1) % 2 == 0:
            # list_for_changes.append(Change_list[i][0].title() + Change_list[i][1:])
            list_for_changes.append(Change_list[i].title())
            print(list_for_changes)
        else:
            list_for_changes.append(Change_list[i])
            print(list_for_changes)
    return ' '.join(list_for_changes)


print(upgrade(words))