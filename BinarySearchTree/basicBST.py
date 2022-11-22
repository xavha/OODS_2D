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

    def delete_node(self, root, data):
        if not root:
            return root

        if data != root.val:
            if data > root.val:
                root.right = self.delete_node(root.right, data)
            else:
                root.left = self.delete_node(root.left, data)
        else:
            if root.right is None:
                root = root.left
            elif root.left is None:
                root = root.right
            else:
                temp = self.find_min(root.right)
                root.val = temp.val
                root.right = self.delete_node(root.right, temp.val)
        return root

    '''
     if r is None:
            return r

        if data != r.data:
            if data > r.data:
                r.right = self.delete(r.right, data)
            else:
                r.left = self.delete(r.left, data)
        else:
            if r.right is None:
                r = r.left
            elif r.left is None:
                r = r.right
            else:
                temp = self.minValueNode(r.right)
                r.data = temp.data
                r.right = self.delete(r.right, temp.data)
        return r
    '''

    def find_min(self, node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr

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
            print(root.val, end=' ')
            self.printInorder(root.right)

    def printPreorder(self, root):
        if root:
            print(root.val, end=' ')
            self.printInorder(root.left)
            self.printInorder(root.right)

    def printPostorder(self, root):
        if root:
            self.printInorder(root.left)
            self.printInorder(root.right)
            print(root.val, end=' ')

    def print_bfs(self, root):
        if not root:
            return
        q = [root]

        while q:
            curr = q.pop(0)
            print(curr.val, end=' ')
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)


def main():
    inp = input('Enter input : ').split()
    tree = BST()
    root = None
    for i in inp:
        # print(i)
        root = tree.insert(root, int(i))

    tree.printTree(root)
    print('----------------------------------')
    print('Inorder : ')
    tree.printInorder(root) or print()
    print('----------------------------------')
    print('Preorder : ')
    tree.printPreorder(root) or print()
    print('----------------------------------')
    print('Postorder : ')
    tree.printPostorder(root) or print()
    print('----------------------------------')
    print('BFS : ')
    tree.print_bfs(root) or print()
    print('----------------------------------')
    print('Height : ', end=' ')
    print(tree.findHeight(root))
    root = tree.delete_node(root, 4)
    tree.printTree(root)


if __name__ == '__main__':
    main()
