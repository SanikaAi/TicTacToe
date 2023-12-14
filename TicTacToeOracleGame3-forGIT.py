
import sys
import oracledb
oracledb.init_oracle_client()
connec=oracledb.connect("@localhost/XE")#Add sql username and password
cur=connec.cursor()

class TicTacToe:
    a = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
    b = [0]
    flag = 0
    flag2=0
    s1=[0]
    s2=[0]
    Xw=0
    Ow=0
    Name1=None
    Name2=None
    def O(self):
        print("==============================")
        ccc='O'
        iq="insert into TicTacToe1 values('%s')"
        cur.execute(iq %(self.Name1))
        connec.commit()
        print("O WINS")
        print("Player name = {}".format(self.Name1))
        print("===============================")
        self.Ow=1

    def X(self):
        print("===============================")
        ddd='X'
        iq1="insert into TicTacToe1 values('%s')"
        cur.execute(iq1 %(self.Name2))
        connec.commit()
        print("X Wins")
        print("Player name = {}".format(self.Name2))
        print("=================================")
        self.Xw=1
    def Xwins(self):
        if self.a[1]==self.a[2]==self.a[3]=='X':
            self.dis()
            self.X()
            sys.exit()
        elif self.a[1]==self.a[5]==self.a[9]=='X':
            print("X wins")
            self.dis()
            self.X()
            sys.exit()
        elif self.a[1]==self.a[4]==self.a[7]=='X':
            print("X wins")
            self.dis()
            self.X()
            sys.exit()
        elif self.a[2]==self.a[5]==self.a[8]=='X':
            print("X wins")
            self.dis()
            self.X()
            sys.exit()
        elif self.a[3]==self.a[5]==self.a[7]=='X':
            print("X wins")
            self.dis()
            self.X()
            sys.exit()
        elif self.a[3]==self.a[6]==self.a[9]=='X':
            print("X wins")
            self.dis()
            self.X()
            sys.exit()
        elif self.a[7]==self.a[8]==self.a[9]=='X':
            print("X wins")
            self.dis()
            self.X()
            sys.exit()
        elif self.a[4]==self.a[5]==self.a[6]=='X':
            print("X wins")
            self.dis()
            self.X()
            sys.exit()

    def Owins(self):
        if self.a[1]==self.a[2]==self.a[3]=='O':
            print("O wins")
            self.dis()
            self.O()
            sys.exit()
        elif self.a[1]==self.a[5]==self.a[9]=='O':
            print(" O wins")
            self.dis()
            self.O()
            sys.exit()
        elif self.a[1]==self.a[4]==self.a[7]=='O':
            print("O wins")
            self.dis()
            self.O()
            sys.exit()
        elif self.a[2]==self.a[5]==self.a[8]=='O':
            print("O wins")
            self.dis()
            self.O()
            sys.exit()
        elif self.a[3]==self.a[5]==self.a[7]=='O':
            print("O wins")
            self.dis()
            self.O()
            sys.exit()
        elif self.a[3]==self.a[6]==self.a[9]=='O':
            print("O wins")
            self.dis()
            self.O()
            sys.exit()
        elif self.a[7]==self.a[8]==self.a[9]=='O':
            print("O wins")
            self.dis()
            self.O()
            sys.exit()
        elif self.a[4]==self.a[5]==self.a[6]=='O':
            print("O wins")
            self.dis()
            self.O()
            sys.exit()




    def dis(self):
        print("{} | {} | {}".format(self.a[1], self.a[2], self.a[3]))
        print("--|---|---")
        print("{} | {} | {}".format(self.a[4], self.a[5], self.a[6]))
        print("--|---|---")
        print("{} | {} | {}".format(self.a[7], self.a[8], self.a[9]))

    def abc(self):
        if self.flag == 0:
            c = int(input("O's chance enter number:"))
            self.flag = 1
            for i in self.b:
                if c==i:
                    self.flag2=1
            if self.flag2!=1:
                self.b.append(c)
                f={c:"O"}
                self.a.update(f)
                self.Owins()
                self.dis()
                self.flag2=0
            else:
                print("Already taken")
                self.flag=0
                self.flag2=0
                self.abc()
        else: #when flag==1
            c = int(input("X's chance enter number:"))
            self.flag = 0
            for i in self.b:
                if c==i:
                    self.flag2=1
            if self.flag2!=1:
                self.b.append(c)
                f={c:"X"}
                self.a.update(f)
                self.Xwins()
                self.dis()
                self.flag2==0
            else:
                print("Already taken")
                self.flag=1
                self.flag2=0
                self.abc()
    def CreateTable(self,dayname):
        iq="create table {} (WinnerName char(2)) ".format(dayname)
        cur.execute(iq)


print("1.New game")
print("2.Show Previous Winners")
print("4.Store list of previous winners in file and store it in another database")
print("5.Copy some data of database in another database")
print("3.Clear previous records")
dec=int(input("Enter your choice:"))
if dec==1:
    T=TicTacToe()
    T.Name1=input("Enter 1st player name :")
    T.Name2=input("Enter 2nd Player name: ")
    print("O is first player and X is second Player")
    print("Let's Start the game")
    print("="*50)
    T.dis()
    for i in range(0,9):
        T.abc()
        if T.Xw!=1 and T.Ow!=1:
            print("No one wins")
elif dec==2:
    cur.execute("select * from TicTacToe")
    rec=0
    while(True):
        rec=rec+1
        record=cur.fetchone()
        if(record!=None):
            for reval in record:
                print("{}".format(reval))
        else:
            break
connec.commit()




