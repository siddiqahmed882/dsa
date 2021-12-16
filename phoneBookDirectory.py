class ContactNode:
    def __init__(self, name, cell):
        self.name = name
        self.cell = cell
        self.prev = None
        self.next = None

    def __str__(self):
        return 'Name: ' + self.name + '\n' + 'Cell: ' + self.cell


class PhoneBookDirectory:
    def __init__(self):
        self.rear = self.front = None

    def addContact(self, name, cell):
        temp = ContactNode(name, cell)
        if self.front is None:
            self.rear = self.front = temp
        elif self.rear == self.front:
            self.rear.next = temp
            temp.prev = self.rear
            self.front = temp
        else:
            temp.prev = self.front
            self.front.next = temp
            self.front = temp

    def searchContact(self, name):
        temp = self.rear
        while True:
            if temp.name == name:
                return temp
            if (not temp.next is None):
                temp = temp.next
            else:
                return 0

    def removeContact(self, name):
        found = self.searchContact(name)
        if found == 0:
            return 'Contact Not exist...'
        prevNode = found.prev
        nextNode = found.next
        if (not prevNode is None):
            prevNode.next = nextNode
        else:
            self.rear = found.next
        if (not nextNode is None):
            nextNode.prev = prevNode
        else:
            self.front = found.prev
        del found
        return 'Contact Removed....'

    def printAll(self):
        temp = phoneBook.rear
        while True:
            print(temp)
            if (not temp.next is None):
                temp = temp.next
            else:
                break


phoneBook = PhoneBookDirectory()
phoneBook.addContact('Siddiq', '03048349985')
phoneBook.addContact('Anas', '03048349984')
phoneBook.addContact('Ibrahim', '03048349986')
phoneBook.addContact('Zaryab', '03048349987')
