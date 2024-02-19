myString = "01234567"
i = 0
while i < len(myString)/2:
    print(''.join(myString[i:i+1] + myString[i+2:i+3]))
    i += 1
