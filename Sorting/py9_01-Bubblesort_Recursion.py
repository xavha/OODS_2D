def bubblesort(lst: list, n, i=1):
    if n == 1:
        return lst
    elif n == i:
        return bubblesort(lst, n-1)
    else:
        if lst[i-1] > lst[i]:
            lst[i-1], lst[i] = lst[i], lst[i-1]
        return bubblesort(lst, n, i+1)


def main():
    inp = list(map(int, input('Enter Input : ').split()))
    lst = bubblesort(inp, len(inp))
    print(lst)


if __name__ == '__main__':
    main()
