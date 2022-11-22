def fgv(lst: list, key: int, i=0):
    if i == len(lst):
        print('No First Greater Value')
        return
    if lst[i] > key:
        print(lst[i])
    else:
        return fgv(lst, key, i+1)


inp = input('Enter Input : ').split('/')
arr, right_arr = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for i in right_arr:
    fgv(sorted(arr), i)
