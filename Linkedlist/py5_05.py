class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        strOut = ''
        while (temp):
            strOut += str(temp.data) + ' -> '
            temp = temp.next
        strOut = strOut[:-4]
        return strOut

    def printWithoutArrow(self):
        temp = self.head
        strOut = ''
        while (temp):
            strOut += str(temp.data) + ' '
            temp = temp.next
        strOut = strOut[:-1]
        return strOut

    def isEmpty(self):
        return self.head == None

    def peekFront(self):
        return self.head.data

    def peekLast(self):
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        return tmp.data

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = Node(data)

    def append_Head(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertSort(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head
        if data < temp.data:
            self.append_Head(data)
            return

        while temp.next is not None:
            if data < temp.next.data:
                break
            temp = temp.next

        if temp.next is None:
            self.append(data)
            return

        newNode = Node(data)
        newNode.next = temp.next
        temp.next = newNode

    def removeFront(self):
        temp = self.head
        if temp is None:
            return
        self.head = temp.next

        return temp.data

    def removeBack(self):
        temp = self.head
        if temp is None:
            return

        if temp.next is None:
            value = temp.data
            self.head = None
            return value

        prev = None
        while temp.next is not None:
            prev = temp
            temp = temp.next

        value = temp.data
        prev.next = None
        return value

    def size(self):
        n = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            n += 1
        return n


def printList(H):
    ll = []
    while H:
        ll.append(str(H.data))
        H = H.next
    print(' '.join(ll))


def radix_sort(llist):
    modder = 10
    divider = 1
    num_llist = [LinkedList() for i in range(10)]
    round = 1
    temp = llist.head
    print_llist = LinkedList()
    num = 0

    tmp = llist.head
    while tmp:
        print_llist.append(tmp.data)
        tmp = tmp.next

    listTemp = LinkedList()
    neg_llist, pos_llist = LinkedList(), LinkedList()
    while not llist.isEmpty():
        if llist.peekFront() >= 0:
            pos_llist.append(llist.removeFront())
        else:
            neg_llist.append(llist.removeFront())

    while not neg_llist.isEmpty():
        listTemp.append_Head(neg_llist.removeBack())
    while not pos_llist.isEmpty():
        listTemp.append(pos_llist.removeFront())

    llist = listTemp

    while 1:
        temp = llist.head
        while temp is not None:
            if temp.data >= 0:
                num = (temp.data % modder) // divider
            else:
                num = (-temp.data % modder) // divider

            num_llist[num].append(temp.data)
            temp = temp.next

        if num_llist[0].size() == llist.size() and len(str(num_llist[0].peekFront())) <= round and len(str(num_llist[0].peekLast())) <= round:
            llist = num_llist[0]
            print('------------------------------------------------------------')
            print(round-1, 'Time(s)')
            print("Before Radix Sort :", print_llist)
            print("After  Radix Sort :", llist)
            return

        print('------------------------------------------------------------')
        print('Round :', round)

        for i in range(len(num_llist)):
            print(i, ":", num_llist[i].printWithoutArrow())

        listTemp = LinkedList()
        for i in range(len(num_llist)):
            neg_llist, pos_llist = LinkedList(), LinkedList()
            while not num_llist[i].isEmpty():
                if num_llist[i].peekFront() >= 0:
                    pos_llist.append(num_llist[i].removeFront())
                else:
                    neg_llist.append(num_llist[i].removeFront())

            while not neg_llist.isEmpty():
                listTemp.append_Head(neg_llist.removeBack())
            while not pos_llist.isEmpty():
                listTemp.append(pos_llist.removeFront())
        llist = listTemp

        modder *= 10
        divider *= 10
        round += 1


if __name__ == '__main__':
    L = LinkedList()

    inp = list(map(int, input("Enter Input : ").split()))
    for i in inp:
        L.append(i)
    radix_sort(L)
