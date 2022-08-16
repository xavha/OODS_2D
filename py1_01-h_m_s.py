print("*** Converting hh.mm.ss to seconds ***")
#print("Enter hh mm ss : ")
#h,m,s = input("Enter hh mm ss : ").split()
h,m,s = [int(h) for h in input("Enter hh mm ss : ").split()]
min="{:,}".format((h*60*60)+(m*60)+s)
if (m>=60 or m<0) :
    print("mm"+"("+str(m)+")"+" is invalid!")
elif (h>24 or h<0) :
    print("hh"+"("+str(h)+")"+" is invalid!")
elif (s>=60 or s<0) :
    print("ss"+"("+str(s)+")"+" is invalid!")
else :
    print(f'{h:02}'+":"+format(m,'02')+":"+format(s,'02')+" = "+min+" seconds")