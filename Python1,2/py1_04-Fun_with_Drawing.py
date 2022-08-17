print("*** Fun with Drawing ***")
n = int(input("Enter input : "))

for i in range (n*2-2,-1,-1):
    for j in range (-1*n*2+2,-1*i):
        if j%2==0 :
            print("#",end='')
        else :
            print(".",end='')
    for j in range (i*2,-1,-1):
        if i%2==0 :    
            print("#",end='')
        else :
            print(".",end='')
    for j in range (-1*n*2+2,-1*i):
        if i%2==0 :
            if j%2==0 :
                print(".",end='')
            else :
                print("#",end='')
        else :
            if j%2==0 :
                print("#",end='')
            else :
                print(".",end='')
    print()

for i in range (1,n*2-1):
    for j in range (-1*n*2+2,-1*i):
        if j%2==0 :
            print("#",end='')
        else :
            print(".",end='')
    for j in range (i*2,-1,-1):
        if i%2==0 :    
            print("#",end='')
        else :
            print(".",end='')
    for j in range (-1*n*2+2,-1*i):
        if i%2==0 :
            if j%2==0 :
                print(".",end='')
            else :
                print("#",end='')
        else :
            if j%2==0 :
                print("#",end='')
            else :
                print(".",end='')
    print()
