secret = 6

while True:
    guess = int(input("Enter a number between 0 and 10: "))
    if guess == secret:
        print("Well done!")
        break
    elif guess < secret:
        print("Your guess is too small. Try again.")
    else:
        print("Your guess is too big. Try again.")
