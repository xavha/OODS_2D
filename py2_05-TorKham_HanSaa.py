class torkham:
    def __init__(self):
        self.wordList = []

    def next(self, word):
        if self.wordList == []:
            self.wordList.append(word)
            print('\''+str(word)+'\' ->',self.wordList)
        else:
            if self.wordList[len(self.wordList)-1][-1].casefold()==word[1].casefold() and self.wordList[len(self.wordList)-1][-2].casefold()==word[0].casefold():
                self.wordList.append(word)
                print('\''+str(word)+'\' ->',self.wordList)
            else:
                print('\''+str(word)+'\' -> game over')
    
    def restart(self):
        self.wordList = []
        print("game restarted")


print("*** TorKham HanSaa ***")
a = list(map(str,input("Enter Input : ").split(",")))
Torkham=torkham()

for i in a:
    word = i.split()
    if word[0] == 'P' :
        Torkham.next(word[1])
    elif word[0] == 'R' :
        Torkham.restart()
    elif word[0] == 'X' :
        exit()
    else :
        print('\''+' '.join(word)+'\' is Invalid Input !!!')
        break