class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)

    def getsize(self):
        return len(self.queue)

    def is_Empty(self):
        return self.queue == []

    def getData(self):
        return self.queue


minOne = minTwo = 0
starOne = starTwo = 0


def cashier(data):
    global minOne, minTwo, starOne, starTwo
    if starOne:
        minOne += 1
        if minOne % 3 == 0 and minOne != 0 and (not cashierOne.is_Empty()):
            cashierOne.dequeue()
            minOne = 0
            if cashierOne.is_Empty():
                starOne = False

    if starTwo:
        minTwo += 1
        if minTwo % 2 == 0 and minTwo != 0 and (not cashierTwo.is_Empty()):
            cashierTwo.dequeue()
            minTwo = 0
            if cashierOne.is_Empty():
                starTwo = False

    if data != ' ':
        if cashierOne.getsize() < 5:
            cashierOne.enqueue(data)
            starOne = True
        else:
            cashierTwo.enqueue(data)
            starTwo = True


inp = input('Enter people and time : ').split()

mainQ = Queue()
cashierOne = Queue()
cashierTwo = Queue()

comm = inp[0].split()
for i in inp[0]:
    mainQ.enqueue(i)

for i in range(int(inp[1])):
    if not mainQ.is_Empty():
        cashier(inp[0][i])
        mainQ.dequeue()
    else:
        cashier(' ')
    print(f'{i+1} {mainQ.getData()} {cashierOne.getData()} {cashierTwo.getData()}')
