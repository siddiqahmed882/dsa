def createNode(number, index):
    return [number, index]


linkedList = []

print("Keep Entring the number. Enter 'N' to exit")
while len(linkedList) <= 10:
    try:
        number = int(input("Enter number: "))
        newNode = createNode(int(number), None)
        if len(linkedList) > 0:
            linkedList[-1][1] = len(linkedList)
        linkedList.append(newNode)
    except:
        print("bad input")
        continue


print(linkedList)
