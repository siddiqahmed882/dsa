def insertionSortInAsc(myList):
    lengthOfArray = len(myList)
    for i in range(1, lengthOfArray):
        value = myList[i]
        pos = i
        while pos > 0 and value < myList[pos - 1]:
            myList[pos] = myList[pos - 1]
            pos -= 1
        myList[pos] = value


def insertionSortInDesc(myList):
    lengthOfArray = len(myList)
    for i in range(1, lengthOfArray):
        value = myList[i]
        pos = i
        while pos > 0 and value > myList[pos - 1]:
            myList[pos] = myList[pos - 1]
            pos -= 1
        myList[pos] = value


nums = [3, 9, 6, 1, 2, 55, 66, 85, 25, 24, 65]
insertionSortInDesc(nums)
print(nums)
