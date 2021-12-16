class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)

    def peek(self):
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()


s = Stack()

string = input("Enter a string: ")
a = ""
l = len(string)
i = l
for i in string:

    s.push(i)

while not s.isEmpty():
    print(s.pop())
