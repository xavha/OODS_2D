class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.lastnode = None

    def add_end(self, data):
        if self.lastnode is None:
            self.head = Node(data)
            self.lastnode = self.head
        else:
            self.lastnode.next = Node(data)
            self.lastnode = self.lastnode.next

    def add_begin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        if not self.lastnode:
            self.lastnode = self.head

    def remove(self, key):
        current = self.head
        # ลบ data ที่ head
        if current.data == key:
            self.head = self.head.next
            return
        # หา data ใน linked list
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next
        # ไม่มี data ที่จะลบ
        if current is None:
            return

        prev.next = current.next
        current = None

    def printlist(self):
        strlist = ''
        current = self.head
        while current.next is not None:
            strlist += str(current.data) + '->'
            current = current.next
        strlist += str(current.data)
        return strlist


def main():
    lst = Linkedlist()
    inp = input('Enter : ').split(',')
    for i in inp:
        cm = i.split()
        if cm[0] == 'Ab':
            lst.add_begin(int(cm[1]))
        elif cm[0] == 'Ae':
            lst.add_end(int(cm[1]))
        else:
            lst.remove(int(cm[1]))
        print(lst.printlist())


if __name__ == '__main__':
    main()
