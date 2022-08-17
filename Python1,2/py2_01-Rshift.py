def Rshift(num,shift):
    global l
    total=0
    l=[]
    if num>=0 :
        pos = 1
    else : 
        pos = 0
        num*=-1
    while num>=1 :
        l.insert(0,num%2)
        num=num//2
        # print(num)
    for i in range (len(l)-shift) :
            total += l[i]*pow(2,(len(l)-shift-i-1))
    if pos==0 :
        if total==0 :
            total-=1
        else :
            total*=-1
    return total      

n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))
