def GCD(a, b):
    if b == 0:
        return a
    if a % b == 0:
        if b < 0:
            return -b
        else:
            return b
    else:
        return GCD(b, a % b)


def main():
    x, y = input('Enter Input : ').split()
    if int(x) < int(y):
        x, y = y, x

    if int(x) == int(y) == 0:
        print('Error! must be not all zero.')
    else:
        print(f'The gcd of {x} and {y} is : {GCD(int(x), int(y))}')


if __name__ == '__main__':
    main()
