import random
import datetime
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                                                                                  TYPE SPEED                                                                                                        ")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
ch=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nu=["1","2","3","4","5","6","7","8","9","0"]
to=ch+nu
start=input("let us start press enter ")
time=[]
timesec=[]
stop=1
score=0
for x in range(1000000000):
    y=datetime.datetime.now()
    if(int(str(y)[17:19])==0):
        print("go")
        break
while(stop!=0):
    z=random.randrange(1,len(to))
    ch=to[z]
    print("-----------------------------",ch,"-----------------------------")
    en=input()
    if(en==ch):
        stop=1
        score+=1
    elif(en!=ch):
        break
    x=datetime.datetime.now()
    st=str(x)
    tim=int(st[14:16])
    sec=int(st[17:19])
    time.append(tim)
    timesec.append(sec)
    if(score!=1):
        if(tim>=time[0]+1 ):
            print("time up")
            break
print("your score is ",score)
    
