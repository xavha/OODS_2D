class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_Empty():
            return 'Empty'
        else:
            return self.queue.pop(0)

    def getsize(self):
        return len(self.queue)

    def is_Empty(self):
        return self.queue == []

    def getData(self):
        return self.queue


inp = input('Enter Input : ').split('/')
comm = inp[0].split(',')
comp = inp[1].split(',')
typeId = []
waiting = []
a = {}

Q = Queue()

for i in comm:
    cm = i.split()
    typeId.append(((cm[1]), (cm[0])))

d = dict(typeId)

for i in comp:
    cm = i.split()
    if cm[0] == 'E':
        waiting.append(((cm[1]), (d[cm[1]])))
    else:
        a = dict(waiting)
        a = sorted(a.items(), key=lambda x: x[1])
        for i in range(len(waiting)):
            Q.enqueue(a[i][0])
        a = {}
        waiting = []
        print(Q.dequeue())
