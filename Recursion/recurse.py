def print2n(num):
    if num > 0:
        print2n(num-1)
        print(num)


def findmin(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        lst.remove(lst[1]) if lst[0] < lst[1] else lst.remove(lst[0])
        return findmin(lst)


def Palindrome(inp):
    if len(inp) <= 1:
        return 'is palindrome'
    else:
        if inp[0] == inp[-1]:
            inp.pop()
            inp.pop(0)
            return Palindrome(inp)
        else:
            return 'is not palindrome'


def Gcd(max, min):
    if min == 0:
        if max < 0:
            return -max
        return max
    else:
        return Gcd(min, max % min)


def Clearstr(str, l, i):
    if i == len(str):
        return l
    else:
        if str[i] >= 'a' and str[i] <= 'z':
            l.append(str[i])
        return Clearstr(str, l, i+1)


def main_findmin():
    inp = input('Enter number : ').split()
    print(findmin(inp))


def main_palindrome():
    inp = input('Enter Input : ')
    list_inp = Clearstr(inp.lower(), [], 0)
    print(f"'{''.join(inp)}' {Palindrome(list_inp)}")


def main_gcd():
    inp = input('Enter Input : ').split()
    print(Gcd(int(inp[0]), int(inp[1]))) if inp[0] > inp[1] else print(
        Gcd(int(inp[1]), int(inp[0])))


def main_sort():
    inp = list(map(int, (input('Enter Input : ').split())))
    # print(sort_listmintomax(inp))


if __name__ == '__main__':
    # main_findmin()
    main_palindrome()
    # main_gcd()
    # main_sort()
