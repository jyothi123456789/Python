str1="Welcome EKIP IT @ madhapure  the session starts at 10:10 a.m"
num=""
alpha=""
special=""
upper=""
for i in range (0,len(str1)):
    if str1[i].isdigit():
        num=num +str1[i]
        elif ((str1[i]>="A"AND STR1[I]<="Z")):
        alpha+=str1[i]
    elif(str1[i]>="a" and str1[i]<="z")):
        print("special character:",i)
    else:
        pass
        # print(i)
