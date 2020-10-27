def moveToFront(list1):
    value = list1.pop()
    return [value,*list1]


li = [1,2,3,4,5]

print(moveToFront(li))