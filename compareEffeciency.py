import timeit

createNode = lambda number, index: [number, index]


def insertInLinkedList(linkedList, node):
    linkedList.insert(0, node)
    for i in range(len(linkedList)):
        if i == len(linkedList) - 1:
            continue
        linkedList[i][1] = i + 1
    return linkedList


def insertInArray(array, number):
    array.insert(0, number)
    return array


linkedList = [[50, 1], [20, 2], [30, None]]
array = [50, 20, 30]

userInput = int(input("Enter number: "))

# keep record for program start time
start = timeit.default_timer()
linkedList = insertInLinkedList(linkedList, createNode(userInput, 0))
print(linkedList)
stop = timeit.default_timer()
print("Time: ", stop - start)

# keep record for program start time
start = timeit.default_timer()
array = insertInArray(array, userInput)
print(array)
stop = timeit.default_timer()
print("Time: ", stop - start)
