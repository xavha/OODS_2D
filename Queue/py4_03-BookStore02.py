class Queue:
    def __init__(self, list=None):
        if list == None:
            self.queue = []
        else:
            self.queue = list

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)

    def getsize(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []


inp = input('Enter Input : ').split('/')
Q = Queue()
for i in inp[0].split():
    Q.enqueue(i)

for i in inp[1].split(','):
    cmd = i.split()
    if cmd[0] == 'D':
        Q.dequeue()
    elif cmd[0] == 'E':
        Q.enqueue(cmd[1])
if len(set(Q.queue)) == Q.getsize():
    print('NO Duplicate')
else:
    print('Duplicate')
