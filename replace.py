list1 = [10, 20,  30, 40]

for i in list1:
    if i == 20:
        list1.remove(20)
        list1[i].extend([30])
        
print(list1)