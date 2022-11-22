def insertion(lst, n=0, i=0):
    if n == len(lst):
        return lst
    if i <= n:
        if lst[n] > lst[i]:
            return insertion(lst, n, i+1)
        else:
            tmp = lst[n]
            lst.remove(lst[n])
            lst.insert(i, tmp)
            return insertion(lst, n+1)


def median(lst):
    lst = insertion(lst)
    if len(lst) % 2 == 1:
        return lst[len(lst)//2]/1
    else:
        return (lst[len(lst)//2]+lst[len(lst)//2-1])/2


def main():
    l = [e for e in input("Enter Input : ").split()]
    if l[0] == 'EX':
        Ans = "quick sort"
        print("Extra Question : What is a suitable sort algorithm?")
        print("   Your Answer : "+Ans)
    else:
        l = list(map(int, l))
        for i in range(len(l)):
            print(f'list = {l[:i+1]} : median = {median(l[:i+1])}')


if __name__ == '__main__':
    main()
