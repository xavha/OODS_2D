class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def sift_up(self, i):
        Stop = False
        while (i // 2 > 0) and Stop == False:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i //
                                                  2] = self.heap_list[i // 2], self.heap_list[i]
            else:
                Stop = True
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)

    def sift_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1

    def delete_min(self):
        if len(self.heap_list) == 1:
            return 'Empty heap'

        root = self.heap_list[1]

        self.heap_list[1] = self.heap_list[self.current_size]

        *self.heap_list, _ = self.heap_list

        self.current_size -= 1

        self.sift_down(1)

        return root

    def print(self):
        return self.heap_list


def main():
    k, lst = input('Enter Input : ').split('/')
    lstBook = [int(i) for i in lst.split()]
    print(lstBook)
    heap = MinHeap()
    for i in range(1, int(k)+1):
        heap.insert(i)
    while lstBook is not None:
        # Customer 1 Booking Van 1 | 3 day(s)
        day = lstBook.pop

if __name__ == '__main__':
    main()

# my_heap = MinHeap()
# my_heap.insert(6)
# my_heap.insert(7)
# my_heap.insert(13)
# my_heap.insert(5)
# my_heap.insert(9)
# my_heap.insert(11)
# my_heap.insert(10)

# print(my_heap.print())
