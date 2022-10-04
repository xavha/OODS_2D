class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        linklist_str = []
        if self.head is None:
            return 'linked list : '
        current = self.head
        linklist_str.append(current.data)
        while current.next is not None:
            current = current.next
            linklist_str.append(current.data)
        linklist_str = '->'.join(linklist_str)
        return f'linked list : {linklist_str}'

    def str_reverse(self):
        linklist_str = []
        if self.tail is None:
            return 'reverse : '
        current = self.tail
        linklist_str.append(current.data)
        while current.previous is not None:
            current = current.previous
            linklist_str.append(current.data)
        linklist_str = '->'.join(linklist_str)
        return f'reverse : {linklist_str}'

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def add_before(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.previous = new_node
            new_node.previous = None
            self.head = new_node
        self.size += 1

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, index, data):
        temp_index = index
        if index < 0 or index > self.size:
            return 'Data cannot be added'

        if self.size == index:
            new_node = Node(data)
            if self.head is None:
                self.head = Node(data)
                self.tail = self.head
            else:
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node
                self.tail.next = None
            self.size += 1
            return f'index = {index} and data = {data}'

        current = self.head

        while current.next is not None:
            if temp_index == 0:
                new_node = Node(data)
                if current == self.head:
                    new_node.next = self.head
                    self.head.previous = new_node
                    new_node.previous = None
                    self.head = new_node
                else:
                    new_node.previous = current.previous
                    current.previous.next = new_node
                    new_node.next = current
                    current.previous = new_node
                self.size += 1
                return f'index = {index} and data = {data}'
            else:
                current = current.next
                temp_index -= 1

        new_node = Node(data)
        new_node.next = self.head
        self.head.previous = new_node
        new_node.previous = None
        self.head = new_node
        self.size += 1
        return f'index = {index} and data = {data}'

    def remove(self, data):
        i = 0
        if self.head is None:
            return 'Not Found!'

        if self.head.data == data:
            if self.tail.data == data:
                self.tail = self.head = None
            else:
                self.head = self.head.next
                self.head.previous = None
            self.size -= 1
            return f'removed : {data} from index : {i}'
        elif self.tail.data == data:
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -= 1
            return f'removed : {data} from index : {self.size-1}'

        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                current.next.previous = current
                self.size -= 1
                return f'removed : {data} from index : {i}'
            else:
                current = current.next
                i += 1

        return 'Not Found!'


def main():
    dlst = DoublyLinkedlist()
    inp = input('Enter : ').split(',')

    for i in inp:
        cm = i.split()
        if cm[0] == 'A':
            dlst.append(cm[1])
        elif cm[0] == 'Ab':
            dlst.add_before(cm[1])
        elif cm[0] == 'I':
            cmm = cm[1].split(':')
            print(dlst.insert(int(cmm[0]), cmm[1]))
        elif cm[0] == 'R':
            print(dlst.remove(cm[1]))
        else:
            pass
        print(dlst.__str__())
        print(dlst.str_reverse())


if __name__ == '__main__':
    main()
