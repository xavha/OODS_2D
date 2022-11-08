class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if root is None:
            return Node(val)
        if root.val == val:
            return root
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def findHeight(self, root):
        if root is None:
            return -1
        height_left = self.findHeight(root.left)
        height_right = self.findHeight(root.right)

        return max(height_left, height_right)+1

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.val)
            self.printInorder(root.right)

    def printPreorder(self, root):
        if root:
            print(root.val)
            self.printInorder(root.left)
            self.printInorder(root.right)

    def printPostorder(self, root):
        if root:
            self.printInorder(root.left)
            self.printInorder(root.right)
            print(root.val)


def main():
    inp = input('Enter input : ').split()
    tree = BST()
    root = None
    for i in inp:
        # print(i)
        root = tree.insert(root, int(i))

    print('Tree : ')
    tree.printTree(root)
    print('----------------------------------')
    print('Inorder : ')
    tree.printInorder(root)
    print('----------------------------------')
    print('Preorder : ')
    tree.printPreorder(root)
    print('----------------------------------')
    print('Postorder : ')
    tree.printPostorder(root)
    print('----------------------------------')
    print('Height : ', end=' ')
    print(tree.findHeight(root))


if __name__ == '__main__':
    main()
