class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data


def createList(l=[]):
    size = 1
    for i in l:
        new_node = node(i)
        if size == 1:
            nodes = new_node
        else:
            tmp = nodes
            while tmp.next:
                tmp = tmp.next
            tmp.next = new_node
        size += 1
    return nodes


def printList(H):
    ll = []
    while H:
        ll.append(H.data)
        H = H.next
    print(' '.join(ll))


def mergeOrderesList(p, q):
    size = 1
    while p and q:
        if size == 1:
            if int(p.data) > int(q.data):
                merge_node = node(q.data)
                q = q.next
            else:
                merge_node = node(p.data)
                p = p.next
            head = merge_node
        else:
            if int(p.data) > int(q.data):
                merge_node.next = node(q.data)
                q = q.next
            else:
                merge_node.next = node(p.data)
                p = p.next
            merge_node = merge_node.next
        size += 1

    if p or q:
        merge_node.next = p if p else q

    return head

    ### Code Here ###

    #################### FIX comand ####################
    # input only a number save in L1,L2
inp = input('Enter 2 Lists : ').split(' ')

L1 = list(inp[0].split(','))
L2 = list(inp[1].split(','))

LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ', end='')
printList(LL1)
print('LL2 : ', end='')
printList(LL2)
m = mergeOrderesList(LL1, LL2)
print('Merge Result : ', end='')
printList(m)
