class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newNode = TreeNode(val)
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

    def postOrder(self, root):
        if(root is not None):
            self.postOrder(root.left)
            self.postOrder(root.right)
            minValue = 0
            if(root.left and root.right):
                minValue = min(root.left.val, root.right.val)
                root.left.val -= minValue
                root.right.val -= minValue
                root.val = minValue
            elif(root.left and not root.right):
                minValue = root.left.val
                root.left.val -= minValue
                root.val = minValue
            elif(root.right and not root.left):
                minValue = root.right.val
                root.right.val -= minValue
                root.val = minValue

    def preOrder(self, root, lst):
        if(root is not None):
            lst.append(root.val)
            self.preOrder(root.left, lst)
            self.preOrder(root.right, lst)
        return lst

    def getRoot(self):
        return self.root


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


a, b = input('Enter Input : ').split('/')
lst = list(map(int, b.split()))

if len(lst) == (int(a)//2)+1:
    T = Tree()
    root = None
    for i in range(1, int(a)+1):
        if i < (int(a)//2)+1:
            root = T.insert(0)
        else:
            root = T.insert(lst[i-((int(a)//2)+1)])
    T.postOrder(root)
    lst = T.preOrder(root, [])
    print(sum(lst))

else:
    print('Incorrect Input')
