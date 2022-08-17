class basicStack():
    def __init__(self):
        self.stack=[]

    def add(self,item):
        self.stack.append(item)
        return f'Add = {item} and Size = {len(self.stack)}'

    def pop(self):
        if self.is_empty():
            return -1
        else:
            return f'Pop = {self.stack.pop()} and Index = {len(self.stack)}'

    def is_empty(self):
        return self.stack == []

    def get_stack(self):
        return self.stack

    def conclusion_stack(self):
        if not self.is_empty():
            string=' '.join(map(str,self.stack))
            return f'Value in Stack = {string}'
        else:
            return f'Value in Stack = Empty'


    

add = list(map(str,input("Enter Input : ").split(",")))
basicstack=basicStack()

for i in add:
    cm=i.split()
    if cm[0]=='A':
        print(basicstack.add(cm[1]))
    else :
        print(basicstack.pop())

print(basicstack.conclusion_stack()) 