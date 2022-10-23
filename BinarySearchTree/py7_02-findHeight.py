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

    def findHeight(self, root):
        if root is None:
            return -1
        else:
            left_height = self.findHeight(root.left)
            right_height = self.findHeight(root.right)

            return max(left_height, right_height) + 1
        # return max(left_height, right_height)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = Node(inp[0])
for i in inp:
    root = T.insert(root, i)
print(f'Height of this tree is : {T.findHeight(root)}')
