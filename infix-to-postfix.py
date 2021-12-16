class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)


operators = ['+', '-', '*', '/', '^', '(', ')']
operatorsPriority = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0, ')': 0}


def checkPriorityAndTakeActions(new, testStack, partialOutput=''):
    prev = testStack.peek()
    if (operatorsPriority[prev] < operatorsPriority[new]):
        testStack.push(new)
        return partialOutput
    else:
        partialOutput += testStack.pop()
        if testStack.isEmpty():
            testStack.push(new)
            return partialOutput
        return checkPriorityAndTakeActions(new, testStack, partialOutput)


# Main Program
testStack = Stack()
expression = input("Enter the expression: ")
output = ''
for i in expression:
    if i in operators:
        if i == '(':
            testStack.push(i)
        elif i == ')':
            while not testStack.isEmpty():
                if testStack.peek() == '(':
                    testStack.pop()
                    break
                else:
                    output += testStack.pop()
        elif testStack.isEmpty():
            testStack.push(i)
        else:
            output += checkPriorityAndTakeActions(i, testStack)
    else:
        output += i
    print(output, testStack)
while not testStack.isEmpty():
    output += testStack.pop()
print(output)
