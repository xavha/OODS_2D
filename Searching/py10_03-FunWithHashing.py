class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class hash:
    def __init__(self, size_table, max_collision):
        self.size_table = size_table
        self.max_collision = max_collision
        self.table = [None for i in range(size_table)]

    def insert(self, key, val):
        self.full()
        idx = tmp_idx = sum(ord(char)for char in key) % self.size_table
        if not self.table[idx]:
            self.table[idx] = Data(key, val)
        else:
            for i in range(self.max_collision):
                idx = (tmp_idx+(i**2)) % self.size_table
                if not self.table[idx]:
                    self.table[idx] = Data(key, val)
                    return
                print(f'collision number {i+1} at {idx}')
            print('Max of collisionChain')

    def full(self):
        if not None in self.table:
            print('This table is full !!!!!!')
            exit()

    def __str__(self):
        s = str()
        for i, val in enumerate(self.table):
            s += f"#{i+1}	{val}\n"
        return s + "---------------------------"


def main():
    print(' ***** Fun with hashing *****')
    inp = input('Enter Input : ').split('/')
    size_tb, max_colli = int(inp[0].split()[0]), int(inp[0].split()[1])
    Hash = hash(size_tb, max_colli)
    for i in inp[1].split(','):
        key, val = i.split()
        Hash.insert(key, val)
        print(Hash)


if __name__ == '__main__':
    main()
