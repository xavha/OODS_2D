class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)

    def checkDuplicate(self):
        # dup = {x for x in self.queue if self.queue.count(x) > 1}
        # if len(dup) == 0 and len(self.queue) != 0:
        #     return f'NO Duplicate'
        # else:
        #     return f'Duplicate'
        for i in self.queue:
            if self.queue.count(i) > 1:
                return "Duplicate"
            else:
                return "NO Duplicate"

    def getQueue(self):
        return self.queue


inp = input('Enter Input : ').split('/')

comm = inp[1].split(',')
comd = inp[0].split()

Q = Queue()

for i in comd:
    Q.enqueue(i)

for i in comm:
    cm = i.split()
    if cm[0] == 'E':
        Q.enqueue(cm[1])
    else:
        Q.dequeue()

print(Q.checkDuplicate())
