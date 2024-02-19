myString = "01234567"
for i in range (len(myString)):
    if i < len(myString)/2:
        print(myString[i : i + 2])



#For i = 0, myString[0:2] prints "01".
#For i = 1, myString[1:3] prints "12".
#For i = 2, myString[2:4] prints "23".
#For i = 3, myString[3:5] prints "34".

