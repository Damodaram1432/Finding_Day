
a=input()
b=int(input())
if a=="sunday":
    day=0
elif a=="monday":
    day=1
elif a=="tuesday":
    day=2
elif a=="wednesday":
    day=3
elif a=="thursday":
    day=4
elif a=="friday":
    day=5
elif a=="saturday":
    day=6
c=(day+(b-1))
c=int(c%7)
if c==0:
    print("sunday")
elif c==1:
    print("monday")
elif c==2:
    print("tuesday")
elif c==3:
    print("wednesday")
elif c==4:
    print("thursday")
elif c==5:
    print("friday")
elif c==6:
    print("saturday")