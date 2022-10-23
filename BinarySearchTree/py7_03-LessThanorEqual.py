class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None
        self.height = 0
        self.c = 0

    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if root.data == data:
                return root
            elif data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
            return root

    def check(self, root: Node, data):
        # if node == None:
        #     return c
        # else:
        #     if node.data == data:
        #         return self.check(node.left, data, c+1)
        #     elif node.data > data:
        #         return self.check(node.left, data, c)
        #     else:
        #         return self.check(node.right, data, c+1)

        # if root is not None:
        #     if int(root.data) <= int(data):
        #         return self.check(root.left, data, c+1)
        #     else:
        #         if int(data) < int(root.data):
        #             return self.check(root.left, data, c)
        #         else:
        #             return self.check(root.right, data, c)
        # else:
        #     return c

        # self.check(root.left,data)

        # self.check(root.right,data)

        if root is not None:
            self.check(root.left, data)
            if int(root.data) <= int(data):
                # print(f'count {root.data}')
                self.c += 1
            self.check(root.right, data)

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = input('Enter Input : ').split('/')
cmm = list(map(int, inp[0].split()))
root = Node(cmm[0])
for i in cmm:
    root = T.insert(root, i)
T.printTree(root)
print('--------------------------------------------------')
T.check(root, int(inp[1]))
print(T.c)
