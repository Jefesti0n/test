f = int(input())
MyList = []

for i in range(f):
    MyList.append(int(input()))
o = int(input())
MyListCopy = MyList.copy()
flag = False
for i in range(len(MyList)):
    for j in MyListCopy[i:]:
        if MyList[i] * MyListCopy[j] == o:
            flag = True
if flag == True:
    print("ДА")
else:
    print("НЕТ")




