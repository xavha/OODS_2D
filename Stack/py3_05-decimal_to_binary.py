class Stack:
    def __init__(self):
        self.stack = []

    def add(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def getStack(self):
        f = ''
        while not self.is_Empty():
            f = f+str(self.pop())+''
        return f

    def is_Empty(self):
        return self.stack == []


def dec2bin(decnum):
    s = Stack()
    while decnum//2 != 0:
        s.add(decnum % 2)
        decnum = decnum//2
    s.add(decnum % 2)
    return s.getStack()


print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ", end='')

print(dec2bin(int(token)))
