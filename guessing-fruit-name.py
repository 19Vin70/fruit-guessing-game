
print("------------------------------------------------------------")
print("                   Welcome to fruit game")
print("------------------------------------------------------------")
print("------------------------------------------------------------")


guess = 2
for i in range(3):
    print("")
    print("Fruit name contains rry")
    print("")
    fruit = input("Enter your guess: ")
    if (fruit == "cherry" or fruit == "Cherry"):
        print("You guessed it correctly!")
        break
    else:
        print(f"{guess} left")
        guess -= 1
        continue
        if(guess <  1):
            break
    
 
guess = 2
for i in range(3):
    print("")
    print("Fruit name contains ana")
    print("")
    fruit = input("Enter your guess: ")
    if (fruit == "banana" or fruit == "Banana"):
        print("You guessed it correctly!")
        break
    else:
        print(f"{guess} left")
        guess -= 1
        continue  
        if(guess < 1):
             break
                     
    
guess = 2
for i in range(3):
    print("")
    print("Fruit name contains ple")
    print("")
    fruit = input("Enter your guess: ")
    if (fruit == "pineapple" or fruit == "Pineapple"):
        print("You guessed it correctly!")
        break
    else:
        print(f"{guess} left")
        guess -= 1
        continue    
        
        
        
     