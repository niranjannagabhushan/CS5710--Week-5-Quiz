myString = "01234567"
j = 0
for i in range(len(myString)):
    if i < len(myString)/2:
        print(''.join(myString[i:i+1] + myString[i+2:i+3]))
    elif j == 0:
        print("STOP")
        j = 1
