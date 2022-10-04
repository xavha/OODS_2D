sour = list()
bitter = list()
ans = list()


def perket(idx, num, b, s, n):
    if(idx == n):
        if(num != 0):
            ans.append(abs(b-s))
        return
    sl = s * int(sour[idx])
    bl = b + int(bitter[idx])
    perket(idx + 1, num, b, s, n)
    perket(idx + 1, num + 1, bl, sl, n)


def main():
    n = input('Enter Input : ').split(',')
    for i in n:
        s, b = i.split()
        sour.append(s)
        bitter.append(b)
    sour.append(0)
    bitter.append(0)
    perket(0, 0, 0, 1, len(n))
    print(min(ans))


if __name__ == '__main__':
    main()
