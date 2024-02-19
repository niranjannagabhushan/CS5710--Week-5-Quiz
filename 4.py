myString = "01234567"
for i in range(len(myString)):
    if i < len(myString)/2:
        print(''.join(myString[i:i+1] + myString[i+2:i+3]))
