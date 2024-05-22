list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list2 = [ 30,40,50]
list1[2][2].extend(list2)
print(list1)

