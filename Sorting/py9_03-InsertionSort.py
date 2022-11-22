def insertion(lst, n=1, i=0):
    if n == len(lst):
        print('sorted')
        print(lst)
        return
    if i <= n:
        if lst[n] > lst[i]:
            return insertion(lst, n, i+1)
        else:
            tmp = lst[n]
            lst.remove(lst[n])
            lst.insert(i, tmp)
            if n == len(lst)-1:
                print(f'insert {tmp} at index {i} : {lst}')
            else:
                print(f'insert {tmp} at index {i} : {lst[:n+1]} {lst[n+1:]}')
            return insertion(lst, n+1)


def main():
    inp = list(map(int, input('Enter Input : ').split()))
    insertion(inp)


if __name__ == '__main__':
    main()
