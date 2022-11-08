class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.total = val

    def __str__(self):
        return str(self.val)


class Tree:
    def __init__(self):
        self.root = None
        self.sum = 0

    def insert(self, val):
        newNode = TreeNode(val)
        self.sum += val
        if(self.root is None):
            self.root = newNode
        else:
            q = [self.root]
            while(len(q) != 0):
                curr = q.pop(0)
                if(curr.left):
                    q.append(curr.left)
                else:
                    curr.left = newNode
                    break
                if(curr.right):
                    q.append(curr.right)
                else:
                    curr.right = newNode
                    break
        return self.root

    def sumBST(self):
        return self.sum

    def rootTotal(self, root):
        if root is not None:
            self.rootTotal(root.left)
            self.rootTotal(root.right)
            if(root.left):
                root.total += root.left.total
            if(root.right):
                root.total += root.right.total

    def mondstadt(self, lst):
        self.rootTotal(self.root)
        q = [self.root]
        while(len(q) != 0):
            curr = q.pop(0)
            lst.append(curr.total)
            if(curr.left):
                q.append(curr.left)
            if(curr.right):
                q.append(curr.right)
        return lst

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


def main():
    T = Tree()
    inp = input('Enter Input : ').split('/')

    for i in inp[0].split():
        T.insert(int(i))

    treelst = T.mondstadt([])
    print(treelst[0])

    comm = [x.split() for x in inp[1].split(',')]
    for i in comm:
        if treelst[int(i[0])] > treelst[int(i[1])]:
            print(f'{i[0]}>{i[1]}')
        elif treelst[int(i[0])] < treelst[int(i[1])]:
            print(f'{i[0]}<{i[1]}')
        else:
            print(f'{i[0]}={i[1]}')


if __name__ == '__main__':
    main()