class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0
        self.loop = False

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            new_node = Node(data)
            current.next = new_node
        self.size += 1

    def set_next(self, index_one, index_two):
        if not self.head:
            return 'Error! {list is empty}'
        if index_one not in range(0, self.size):
            return 'Error! {index not in length}: ' + f'{index_one}'
        if int(index_two) not in range(0, self.size):
            self.append(index_two)
            return 'index not in length, append : ' + f'{index_two}'
        else:
            n1 = self.head
            for _ in range(index_one):
                n1 = n1.next
            n2 = self.head
            for _ in range(int(index_two)):
                n2 = n2.next
            n1.next = n2
        if index_one >= int(index_two):
            self.loop = True
        return f'Set node.next complete!, index:value = {index_one}:{n1.data} -> {index_two}:{n2.data}'

    def print_str(self):
        linklist_str = []
        if self.head is None:
            return 'Empty'
        current = self.head
        linklist_str.append(str(current.data))
        while current.next:
            current = current.next
            linklist_str.append(str(current.data))

        linklist_str = ('->').join(linklist_str)
        return linklist_str

    def check_loop(self):
        if not self.loop:
            return f'No Loop\n{self.print_str()}'
        else:
            return 'Found Loop'


def main():
    ll = Linkedlist()
    inp = input('Enter input : ').split(',')
    for i in inp:
        i = i.split()
        if i[0] == 'A':
            ll.append(i[1])
            print(ll.print_str())
        elif i[0] == 'S':
            cm = i[1].split(':')
            print(ll.set_next(int(cm[0]), str(cm[1])))
    print(ll.check_loop())


if __name__ == '__main__':
    main()
