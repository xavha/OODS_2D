class Data:
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return str(self.key)


class Rehash:
    def __init__(self, size_table, max_collision, treshold):
        self.size_table = size_table
        self.max_collision = max_collision
        self.treshold = treshold
        self.lst_data = []
        self.table = [None for i in range(size_table)]

    def insert(self, key):
        if self.full():
            self.rehashing()
            tmp_lst = self.lst_data
            self.lst_data = []
            for i in tmp_lst:
                self.insert(i)
        idx = tmp_idx = int(key) % self.size_table
        if not self.table[idx]:
            self.table[idx] = Data(key)
            self.lst_data.append(key)
        else:
            for i in range(self.max_collision):
                idx = (tmp_idx+(i**2)) % self.size_table
                if not self.table[idx]:
                    self.table[idx] = Data(key)
                    self.lst_data.append(key)
                    return
                print(f'collision number {i+1} at {idx}')
            print('****** Max collision - Rehash !!! ******')
            self.rehashing()
            tmp_lst = self.lst_data
            self.lst_data = []
            for i in tmp_lst:
                self.insert(i)
            self.insert(key)

    def full(self):
        sum_data = 0
        for i in self.table:
            if i is not None:
                sum_data += 1
        max_data = (self.size_table*self.treshold//100)
        if sum_data >= max_data:
            print('****** Data over threshold - Rehash !!! ******')
            return True
        return False

    def rehashing(self):
        self.size_table = closest_prime(self.size_table*2)
        self.table = [None for i in range(self.size_table)]
        # for i in range(self.size_table - len(self.table)):
        #     self.table.append(None)

    def __str__(self):
        s = str()
        for i, val in enumerate(self.table):
            s += f"#{i+1}	{val}\n"
        return s + "----------------------------------------"


def check_prime(number):
    if number > 1:
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                return False
        return True
    return False


def closest_prime(number):
    for i in range(1, number):
        n = number + i
        if check_prime(n):
            return n


def main():
    print(' ***** Rehashing *****')
    inp = input('Enter Input : ').split('/')
    size_tb, max_colli, threshold = int(inp[0].split()[0]), int(
        inp[0].split()[1]), int(inp[0].split()[2])
    Hash = Rehash(size_tb, max_colli, threshold)
    print('Initial Table :')
    print(Hash)
    for i in inp[1].split():
        print(f'Add : {i}')
        Hash.insert(i)
        print(Hash)


if __name__ == '__main__':
    main()
