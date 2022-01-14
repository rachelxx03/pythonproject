import timeit
start = timeit.default_timer()
pos={n: "_" for n in range (36)}
board=f"[{pos[0]}] [{pos[1]}] [{pos[2]}] [{pos[3]}] [{pos[4]}] [{pos[5]}] " \
      f"[{pos[6]}] [{pos[7]}] [{pos[8]}] [{pos[9]}] [{pos[10]}] [{pos[11]}]\n"\
      f"[{pos[12]}] [{pos[13]}] [{pos[14]}] [{pos[15]}] [{pos[16]}] [{pos[17]}]\n"\
      f"[{pos[18]}] [{pos[19]}] [{pos[20]}] [{pos[21]}] [{pos[22]}] [{pos[23]}]\n"\
      f"[{pos[24]}] [{pos[25]}] [{pos[26]}] [{pos[27]}] [{pos[28]}] [{pos[29]}]\n"\
      f"[{pos[30]}] [{pos[31]}] [{pos[32]}] [{pos[33]}] [{pos[34]}] [{pos[35]}]\n"
print(board)
cablemove=[i for i in range(len(pos)-1)]
lsx=[]
lso=[]
#check if the player win or not
def win_able(test,i):
    for k in range(4):
            dia=[1,6,7,5]
            def win_check(i,dia,k):
                    h=m=i
                    countlef=0
                    countrig=0
                    l=True
                    r=True
                    for j in range(4):
                        h+=dia[k]
                        if r==True:
                            if  k!= 1 :
                                if  ((h+1)%6==0 and (h+1) in test)or (h%6==0 and h in test) :

                                    countrig+=1
                                    r=False
                        if r==True:
                            if h in test :
                                countrig+=1
                            else:
                                 h=i
                                 r=False
                        if l==True:
                            if k!= 1:
                                if ((m+1)%6==0 and (m+1) in test)or (m%6==0 and m in test):

                                    countlef+=1
                                    l=False
                        if l==True:
                            if m in test :
                                countlef+=1
                            else:
                                 m=i
                                 l=False
                            m-=dia[k]
                    print(countlef,countrig)
                    if countlef+countrig>=4:
                        return 1
            result= win_check(i,dia,k)
            if result==1:
                print("you win")
                break
for i in range(36):
    k=int(input("enter a number from 0 to 8 for pos"))
    while k not in cablemove  :
        k=int(input("enter a number from 0 to 8 for pos"))
    if i%2==0 :
        cablemove.remove(k)
        pos.update({k:"X"})
        lsx.append(k)
        result=win_able(lsx,k)
        if result=="you win":
            break
    else:
         cablemove.remove(k)
         pos.update({k:"O"})
         lso.append(k)
         win_able(lso,k)
    board=f"[{pos[0]}] [{pos[1]}] [{pos[2]}] [{pos[3]}] [{pos[4]}] [{pos[5]}]\n" \
          f"[{pos[6]}] [{pos[7]}] [{pos[8]}] [{pos[9]}] [{pos[10]}] [{pos[11]}]\n"\
          f"[{pos[12]}] [{pos[13]}] [{pos[14]}] [{pos[15]}] [{pos[16]}] [{pos[17]}]\n"\
          f"[{pos[18]}] [{pos[19]}] [{pos[20]}] [{pos[21]}] [{pos[22]}] [{pos[23]}]\n"\
          f"[{pos[24]}] [{pos[25]}] [{pos[26]}] [{pos[27]}] [{pos[28]}] [{pos[29]}]\n"\
          f"[{pos[30]}] [{pos[31]}] [{pos[32]}] [{pos[33]}] [{pos[34]}] [{pos[35]}]\n"
    print(board)

