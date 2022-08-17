print("*** multiplication or sum ***")
a = input("Enter num1 num2 : ").split(" ")
if int(a[0])*int(a[1])>1000 :
    print("The result is "+str(int(a[0])+int(a[1])))
else :
    print("The result is "+str(int(a[0])*int(a[1])))