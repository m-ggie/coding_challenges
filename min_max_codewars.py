mylist = [1, 6, 7, 2]

def min_max(lst):
    temphi = lst[0]
    templo = lst[0]
    for n in lst:
        temp = n
        if n > temphi:
            temphi = n
        if n < templo:
            templo = n
    minmax = [templo, temphi]
    return minmax

min_max(mylist)