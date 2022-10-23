class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root: Node, data):
        if root is None:
            return Node(data)

        if root.data == data:
            return root
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def delete(self, r, data):
        if r is None:
            print('Error! Not Found DATA')
            return r

        if data < r.data:
            r.left = self.delete(r.left, data)
        elif data > r.data:
            r.right = self.delete(r.right, data)
        else:
            if r.right is None:
                temp = r.left
                r = None
                return temp
            elif r.left is None:
                temp = r.right
                r = None
                return temp
            # minvalue of right subtree
            temp = self.minValueNode(r.right)
            r.data = temp.data
            r.right = self.delete(r.right, temp.data)

        # printTree90(root)
        return r

    def minValueNode(self, node):
        current = node

        while(current.left is not None):
            current = current.left

        return current


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")

root = None

for i in data:
    cmm = i.split()
    if cmm[0] == 'i':
        print(f'insert {cmm[1]}')
        root = tree.insert(root, int(cmm[1]))
        printTree90(root)
    else:
        print(f'delete {cmm[1]}')
        root = tree.delete(root, int(cmm[1]))
        if root is not None:
            printTree90(root)
