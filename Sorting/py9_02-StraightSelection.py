def straight_select(lst: list, i=0):
    max_index = lst.index(max(lst[:len(lst)-i]))
    if i == len(lst)-1:
        return lst
    if max_index != len(lst)-i-1:
        lst[len(lst)-i-1], lst[max_index] = lst[max_index], lst[len(lst)-i-1]
        print(f'swap {lst[max_index]} <-> {lst[len(lst)-i-1]} : {lst}')
    return straight_select(lst, i+1)


def main():
    inp = list(map(int, input('Enter Input : ').split()))
    lst = straight_select(inp)
    print(lst)


if __name__ == '__main__':
    main()
