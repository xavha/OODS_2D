print("*** Fun with countdown ***")
l = [int(l) for l in input("Enter List : ").split()]

col=[]
countdown=[]
num=0


for i in range(len(l)) :
    temp=l[i]
    if i<=len(l)-2 and l[i]-l[i+1]==1:
        col.append(temp)
    elif l[i]==1 :
        col.append(temp)
        countdown.append(col)
        num+=1
        col=[]
    else :
        col=[]

print([num,countdown])

#  4 4 5 4 3 2 1 8 3 2 1