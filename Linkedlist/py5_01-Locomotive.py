class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next

    def format_print(self):
        current = self.head
        str = ''
        while current is not None and current is not self.last_node:
            str += current.data+' <- '
            current = current.next
        str += current.data
        return f'{str}'

    def alternate(self):
        current = self.head

        if int(current.data) == 0:
            return

        while int(current.next.data) != 0:
            current = current.next

        self.last_node.next = self.head
        self.last_node = self.head
        self.head = current.next
        self.last_node = current
        current.next = None


if __name__ == '__main__':
    print(' *** Locomotive ***')
    inp = input('Enter Input : ').split()

    list = Linkedlist()

    for i in inp:
        list.append(i)

    print('Before : '+list.format_print())

    list.alternate()

    print('After : '+list.format_print())
