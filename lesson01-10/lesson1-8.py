def common(list1, list2):
    return [item for item in list1 if item in list2]
    
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(common(list1,list2))



