def odd_even(type, data, mode):
    istypelist = False
    if type == 'L' :
        istypelist = True
        data = list(data.split(" "))
        temp=[]
    else :
        temp=''
    for i in range (len(data)) :
        if mode=='Odd' :
            if i%2==0 :
                if istypelist : 
                    temp.append(data[i])
                else :
                    temp+=data[i]
        else :
            if i%2==1 :
                if istypelist : 
                    temp.append(data[i])
                else :
                    temp+=data[i]
    return temp

print("*** Odd Even ***")
type,data,mode = input("Enter Input : ").split(",")

print(odd_even(type,data,mode))