class Stack:
    def __init__(self):
        self.stack = []

    def add(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def is_Empty(self):
        return self.stack == []

    def peek(self):
        if self.is_Empty():
            raise Exception("Peeking from an empty stack")
        return self.stack[-1]

    def getSize(self):
        return len(self.stack)

    def getStack(self):
        return ''.join(self.stack)


S = Stack()


def Parenthesis(close):
    if S.is_Empty():
        return f'close paren excess'
    else:
        open = S.peek()

    if open == '(':
        if close == ')':
            return 1
        else:
            return f'Unmatch open-close'
    if open == '[':
        if close == ']':
            return 1
        else:
            return f'Unmatch open-close'
    if open == '{':
        if close == '}':
            return 1
        else:
            return f'Unmatch open-close'


inp = input("Enter expresion : ")

for i in inp:
    if i == '(' or i == '[' or i == '{':
        S.add(i)
    elif i == ')' or i == ']' or i == '}':
        if Parenthesis(i) != 1:
            print(f'{inp} '+Parenthesis(i))
            exit()
        else:
            S.pop()
    else:
        pass

if S.is_Empty():
    print(f'{inp} MATCH')
else:
    print(f'{inp} open paren excess   {S.getSize()} : {S.getStack()}')
