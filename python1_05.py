print("*** Fun with countdown ***")
h= [int(h) for h in input("Enter List : ").split()]
l=[]
sumOne=0

temp = 1
def countdown(temp):
    global l
    while(temp in h) :
        l.append(temp)
        h.remove(temp)
        temp+=1
    temp = 1
    print(l)
    l=[]

for i in range(len(h)) :
    if h[i]==1:
        sumOne+=1

for i in range(sumOne) :
    countdown(temp)



