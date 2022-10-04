def Palindrome(lst):
    if len(lst) <= 1:
        return 'is palindrome'
    else:
        if lst[0] == lst[-1]:
            lst.pop()
            lst.pop(0)
            return Palindrome(lst)
        else:
            return 'is not palindrome'


def main():
    inp = list(input('Enter Input : '))

    print(f"'{''.join(inp)}' {Palindrome(inp)}")


if __name__ == '__main__':
    main()
