class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def append_head(self, data):
        newNode = Node(data)
        newNode.next = self.head

        if self.head != None:
            self.head.previous = newNode
            self.head = newNode
            newNode.previous = None

        else:
            self.head = newNode
            self.tail = newNode
            newNode.previous = None

        self.size += 1

    def insert(self, index, data):
        if index < 0 or int(index) > self.size:
            print('Data cannot be added')
            return
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            self.size += 1
            print(f'index = {index} and data = {data}')
        elif index == 0:
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
            self.size += 1
            print(f'index = {index} and data = {data}')
        elif self.size == index:
            print(f'index = {index} and data = {data}')
            self.append(data)
        else:
            current = self.head
            for i in range(index-1):
                if current is not None:
                    current = current.next
            newNode.previous = current
            newNode.next = current.next
            current.next.previous = newNode
            current.next = newNode
            self.size += 1
            print(f'index = {index} and data = {data}')

    def remove(self, data):
        p = self.head
        i = 0
        while p != None:
            if int(p.data) == int(data):
                if p != self.head and p != self.tail:
                    p.previous.next = p.next
                    p.next.previous = p.previous
                    p.previos = None
                    p.next = None
                elif p == self.head and self.head != self.tail:
                    p.next.previous = None
                    self.head = p.next
                    p.next = None
                elif p == self.tail and self.head != self.tail:
                    p.previos.next = None
                    self.tail = p.previous
                    p.previous = None
                else:
                    self.head = None
                    self.tail = None
                self.size -= 1
                print(f'removed : {data} from index : {i}')
                return()
            p = p.next
            i += 1
        print('Not Found!')

    def __str__(self):
        current = self.head
        str = ''
        if self.isEmpty():
            print(f'linked list : {str}')
            return
        else:
            while current.next is not None and self.size != 1:
                str += current.data+'->'
                current = current.next

            str += current.data
            print(f'linked list : {str}')

    def str_reverse(self):
        current = self.tail
        str = ''
        if self.isEmpty():
            print(f'reverse : {str}')
            return
        else:
            str += current.data
            current = current.previous
            while current is not None:
                str += '->'+current.data
                current = current.previous
            print(f'reverse : {str}')

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    doubly = DoublyLinkedList()
    inp = input('Enter Input : ').split(',')

    for i in inp:
        cm = i.split()
        if cm[0] == 'A':
            doubly.append(cm[1])
        elif cm[0] == 'Ab':
            doubly.append_head(cm[1])
        elif cm[0] == 'I':
            cmm = cm[1].split(':')
            doubly.insert(int(cmm[0]), cmm[1])
        elif cm[0] == 'R':
            data = doubly.remove(int(cm[1]))

        doubly.__str__()
        doubly.str_reverse()
