queue = []

inp = list(input("Enter Input : ").split(","))
for i in inp:
    cm = i.split(' ')
    if cm[0] == 'E':
        print(f'Add {cm[1]} index is {len(queue)}')
        queue.append(cm[1])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(f'Pop {str(queue.pop(0))} size in queue is {len(queue)}')

if len(queue) == 0:
    print('Empty')
else:
    print(f'Number in Queue is :  {queue}')
