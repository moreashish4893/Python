import random

Target = random.randint(1,100)

while True:
    userChoice = input("Guess the Target or Quit:")
    if(userChoice == "Quit"):
        break

    userChoice = int(userChoice)
    if(userChoice == Target):
        print("Success : Correct Guess!! ")

    elif(userChoice < Target):
        print("Your number was small.Take a bigger guess...")

    else:
        print("Your number was big.Take a smaller guess...")    


print("---Game Over---")    