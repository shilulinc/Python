# Author:ShiLU
Tom = 23
print(type(Tom))

count = 0
while count < 3 :
    guess = int(input("guess_age:"))
    print(type(guess))
    if guess == Tom :
        print ("It's OK !")
        break
    elif guess > Tom:
        print("Think smaller !")
    else:
        print("Think bigger !")
    count += 1
    if count == 3 :
        continue_confirm = input("Are you try again ?")
        if continue_confirm != "n" :
            count = 0
#else:
#        print("You try too many times... fuck off !")