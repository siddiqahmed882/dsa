def bubbleSortInAsc(list):
    lengthOfArray = len(list)
    for i in range(lengthOfArray - 1):
        for j in range(lengthOfArray - 1 - i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


def modifiedBubbleSortInAsc(list):
    lengthOfArray = len(list)
    for i in range(lengthOfArray - 1):
        didSwap = False
        for j in range(lengthOfArray - 1 - i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                didSwap = True
        if not didSwap:
            print('Broke on ', i + 1, ' pass')
            break


def bubbleSortInDesc(list):
    lengthOfArray = len(list)
    for i in range(lengthOfArray - 1):
        print(list)
        for j in range(lengthOfArray - 1 - i):
            if list[j] < list[j + 1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


nums = [5, 10, 0, 20]
bubbleSortInAsc(nums)
print('result', nums)

# bubbleSortInDesc(nums)
# print('result', nums)
