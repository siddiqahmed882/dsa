class Dequeue:
    def __init__(self):
        self.items = []

    def insertFromRear(self, data):
        self.items.insert(0, data)

    def insertFromFront(self, data):
        self.items.append(data)

    def removeFromRear(self):
        return self.items.pop(0)

    def removeFromFront(self):
        return self.items.pop(-1)


# initialize dequeue
testDequeue = Dequeue()

string = input("Enter a string to check for palindrome: ")
for i in string:
    testDequeue.insertFromFront(i)
iterations = len(string) // 2
flag = False
for i in range(iterations):
    if (testDequeue.removeFromRear() == testDequeue.removeFromFront()):
        flag = True
    else:
        Flag = False
        break
print('The given string is', ('palindrome' if flag else 'not palindrome'))
