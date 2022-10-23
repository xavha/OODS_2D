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

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            new_node = Node(data)
            curr = self.root

            while (curr.left or curr.right) is not None:
                if data < curr.data and curr.left is not None:
                    curr = curr.left
                elif data > curr.data and curr.right is not None:
                    curr = curr.right
                else:
                    break

            if data < curr.data:
                curr.left = new_node
            else:
                curr.right = new_node

            return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
