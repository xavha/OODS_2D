class Stack:
    def __init__(self):
        self.stack_data=[]
        self.stack_priority=[]

    def push(self, value):
        if self.is_Empty():
            self.stack_data.append(value[0][0])
            self.stack_priority.append(value[0][1])
        else:
            if value[0][0]==')':
                while self.stack_data[-1]!='(':
                    print(self.pop(),end='')
                self.pop()
            else:
                if value[0][1]>self.stack_priority[-1]:
                    self.stack_data.append(value[0][0])
                    self.stack_priority.append(value[0][1])
                elif value[0][0]=='(':
                    self.stack_data.append(value[0][0])
                    self.stack_priority.append(value[0][1])
                else:
                    print(self.pop(),end='')
                    self.push(value)
                
    def pop(self):
        self.stack_priority.pop()
        return self.stack_data.pop()

#     def size(self):

    def is_Empty(self):
        return self.stack_data == []

inp = input('Enter Infix : ')
S = Stack()

print('Postfix : ', end='')

for i in inp:
    if i == '^':
        data=list(zip(i,'3'))
        S.push(data)
    elif i=='*' or i=='/':
        data=list(zip(i,'2'))
        S.push(data)
    elif i=='+'or i=='-':
        data=list(zip(i,'1'))    
        S.push(data)
    elif i=='(' or i==')':
        data=list(zip(i,'0'))
        S.push(data)
    else:
        print(i,end='')
    
while not S.is_Empty():
    print(S.pop(), end='')

print()