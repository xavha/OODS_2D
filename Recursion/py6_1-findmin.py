def Findmin(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        if lst[0] >= lst[1]:
            lst.remove(lst[0])
        else:
            lst.remove(lst[1])
        return Findmin(lst)


def main():
    lst = list(map(int, input("Enter Input : ").split()))
    min = Findmin(lst)
    print(f'Min : {min}')


if __name__ == '__main__':
    main()
