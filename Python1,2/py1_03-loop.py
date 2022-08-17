print(" *** Summation of each digit ***")
b=input("Enter a positive number : ")
x = [int(a) for a in str(b)]
c=0
for i in range(0,len(b)) :
    c=c+x[i]

print("Summation of each digit =  "+str(c))