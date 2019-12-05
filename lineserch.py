def linearSearch(li, x):
    i = 0
    length = len(li)
    while i < length and x != li[i]:
        i += 1
    return i if i < length else None
