def selectionSortInAsc(myList):
    lengthOfArray = len(myList)
    for i in range(lengthOfArray - 1):
        smallIndex = i
        for j in range(i + 1, lengthOfArray):
            if myList[j] < myList[smallIndex]:
                smallIndex = j
        if smallIndex != i:
            temp = myList[i]
            myList[i] = myList[smallIndex]
            myList[smallIndex] = temp


def selectionSortInDesc(myList):
    lengthOfArray = len(myList)
    for i in range(lengthOfArray - 1):
        smallIndex = i
        for j in range(i + 1, lengthOfArray):
            if myList[j] > myList[smallIndex]:
                smallIndex = j
        if smallIndex != i:
            temp = myList[i]
            myList[i] = myList[smallIndex]
            myList[smallIndex] = temp


nums = [3, 9, 6, 1, 2]
selectionSortInAsc(nums)
print(nums)
