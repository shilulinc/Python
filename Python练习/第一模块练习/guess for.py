# Author:ShiLU
Tom = 23
print(type(Tom))

for i in range(3) :
    guess = int(input("guess_age:"))
    print(type(guess))
    if guess == Tom :
        print ("It's OK !")
        break
    elif guess > Tom:
        print("Think smaller !")
    else:
        print("Think bigger !")

else:
        print("You try too many times... fuck off !")