myString = "01234567"
for i in range(len(myString)):
    if i < len(myString)/2:
        print(myString[i] + myString[i + 2])
