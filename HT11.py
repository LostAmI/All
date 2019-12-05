# def Altered(n):
#     if n == 1:
#         return 5
#     if n == 2:
#         return 3
#     return Altered(n - 1) * Altered(n - 2)
#
# print(Altered(5))

def get_total_cost(n):
    if n == 1:
        return 40
    elif n > 10:
        return
        return get_total_cost(n - 1) + (40 - ((40 * 2) / 100))

    return get_total_cost(n - 1) + 40


print(get_total_cost(11))
