# def torkham(word,newgame) :
#     print(newgame)
#     if word[0] == 'P' :
#         if newgame:
#             out=[]
#             out.append(word[1])
#             check=word[1][-2]+word[1][-1]
#             print(out)
#             newgame=False
#         else :
#             if word[1][0]+word[1][1] == check :
#                 out.append(word[1])
#                 print(out)
#     elif word[0] == 'R' :
#         out=[]
#         newgame=True
#         print("game restarted")
#     elif word[0] == 'X' :
#         exit()
#     else :
#         print(" is Invalid Input !!!")
#         exit()

wordlist = []
check = ''

class torkham :
    def __init__(self):
        self.newgame = True
        pass
    def next(self,word) :
        global wordlist,check
        self.newgame = newgame
        self.word = word
        if self.newgame:
            wordlist.append(word)
            check=word[-2]+word[-1]
            print(wordlist)
            self.newgame=False
        else :
            if word[1][0]+word[1][1] == check :
                wordlist.append(word[1])
                print(wordlist)
        pass
    def restart():
        global wordlist,newgame
        newgame=True
        wordlist=[]
        print("game restarted")
        pass
        

    

print("*** TorKham HanSaa ***")
a = input("Enter Input : ").split(",")



for i in range (len(a)) :
    word=a[i].split(" ")
    if word[0] == 'P' :
        torkham.next(word[1])
    elif word[0] == 'R' :
        torkham.restart()
    elif word[0] == 'X' :
        exit()
    else :
        print(" is Invalid Input !!!")
    
    
    # torkham(word,newgame)
    

       
