sour = 1
bitter = 0

pk = lst_parket = []


def Group(lst, size, i):
    global lst_parket
    print(lst)
    if len(lst_parket) == size:
        print('Parket')
        Parket(lst_parket)
        lst_parket = []
    else:
        print('Append')
        lst_parket.append(lst[i])
        print(lst_parket)
        if i <= size:
            Parket(lst_parket)
        Group(lst, size, i+1)
        # def Perket(lst, size):
        #     global sour, bitter

        #         # sour = sour * int(lst[0][0])
        #         # bitter = bitter + int(lst[0][1])
        #         # print(f'{sour} : {lst[0][0]} || {bitter} : {lst[0][1]} - {lst}')
        #     return abs(sour-bitter)


def Parket(lst):
    global sour, bitter, pk
    if lst == []:
        pk.append(abs(sour-bitter))
        print(min(pk))
        return
    else:
        sour = sour * int(lst[0][0])
        bitter = bitter + int(lst[0][1])
        lst.pop(0)
        return Parket(lst)


def main():
    inp = input('Enter Input : ').split(',')
    lst = [item.split(' ') for item in inp]
    Group(lst, len(lst), 0)


if __name__ == '__main__':
    main()
