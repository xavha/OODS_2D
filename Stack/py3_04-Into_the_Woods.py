class Stack:
    def __init__(self):
        self.stack = []

    def add(self, height):
        self.stack.append(height)

    def pop(self):
        self.stack.pop()

    def getSize(self):
        return len(self.stack)

    def is_Empty(self):
        return self.stack == []

    def peek(self):
        return int(self.stack[-1])


S = Stack()

inp = input('Enter Input : ').split(',')

for i in inp:
    cm = i.split()
    if cm[0] == 'A':
        while not S.is_Empty() and S.peek() <= int(cm[1]):
            S.pop()
        S.add(cm[1])
    else:
        print(S.getSize())
