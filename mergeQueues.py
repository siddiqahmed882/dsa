class Queue:
    def __init__(self, arr=None):
        self.items = []
        if arr:
            for elem in arr:
                self.enqueue(elem)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

    def __str__(self):
        return str(self.items)


firstQueue = Queue([0, 2, 4, 6])
secondQueue = Queue([1, 3, 5, 7])
thirdQueue = Queue()
for _ in range(4):
    thirdQueue.enqueue(firstQueue.dequeue())
    thirdQueue.enqueue(secondQueue.dequeue())

print(thirdQueue)
