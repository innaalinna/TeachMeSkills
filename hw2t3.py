import random as r

randInt = r.randint(1, 10)
#print(randInt)

while True:
    try:
        print("Let you try to guess the number between 1 and 10: ")
        guessInt = int(input())

    except ValueError as e:
        print("Please enter number again.")

    else:
        if guessInt == randInt:
            print("You are Wanga!")
            break
        else:
            print("Try ur fortune again!")
            continue



