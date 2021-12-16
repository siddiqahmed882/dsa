class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, data):
        if self.isEmpty() and data == ')':
            return 'First bracket can not be a closing one....'
        if not self.isEmpty() and self.peek() == '(' and data == ')':
            self.items.pop()
            return 'Parenthesis Balanced...'
        self.items.append(data)
        return 'Added...'

    def pop(self):
        self.items.pop(-1)

    def peek(self):
        return self.items[-1]


testStack = Stack()
print("Keep entering '(' OR ')' to check and 0 to exit")
while True:
    userInput = input("Enter.. ")
    if (userInput == '(' or userInput == ')'):
        result = testStack.push(userInput)
        print(result)
    elif(userInput == '0'):
        if testStack.isEmpty():
            print("Paranthesis Balaned....")
        else:
            print("Paranthesis are not balanced\nExiting program....")
        break
    else:
        print("Bad Input")
