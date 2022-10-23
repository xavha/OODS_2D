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

    def insert(self, root, data):
        if root is None:
            self.root = Node(data)
            return Node(data)
        else:
            if root.data == data:
                return root
            elif data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
            return root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self, root, temp, data):
        if root.data == data:
            return print('Root')
        if temp is not None:
            if data < temp.data:
                self.checkpos(root, temp.left, data)
            elif data > temp.data:
                self.checkpos(root, temp.right, data)
            else:
                if temp.right or temp.left:
                    return print('Inner')
                else:
                    return print("Leaf")
        else:
            return print("Not exist")


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]

root = Node(inp[1])

for i in range(1, len(inp)):
    root = T.insert(root, inp[i])
T.printTree(root)
T.checkpos(root, root, inp[0])
