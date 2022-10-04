def staircase(n, num):
    if num == 0:
        return 'Not Draw!'
    if n == 0:
        return ''
    if num < 0:
        return '_'*(-1*(num-n)) + '#'*abs(n) + '\n' + staircase(n+1, num)
    else:
        return '_'*(n-1) + '#'*(num-n+1) + '\n' + staircase(n-1, num)


def main():
    n = int(input("Enter Input : "))
    print(staircase(n, n))


if __name__ == '__main__':
    main()
