import random

words=['robert','berort','mishraji','mijirash','rajit','arjit','krushna','rushank','tanaya','yatana','shradha','dhashra','namita','manita','netra','terna','ashish','shisha','abhishek','shakrbhi','vishal','shalvi']
score=0
while True:
    for wr in range(3):
        lett=list(random.choice(words))
        print("Guess the correct word by given word:=>","".join(lett))
        user= input("enter correct word or '(quit)':")
        if user=='quit':
            break

        if user!="".join(lett):

            valid=True
            for letter in user:
                if letter in lett:
                    lett.remove(letter)
            else:
                valid=False
                break

        if valid and user in words:
            score=score+len(user)
            print(f"correct and your score is {score}")
        else:
            print("wrong word enter by you")
        if user!="".join(lett):
            break
        else:
            print("You entered the same name which we provided...")
    else:
        score=score+len(user)
        print(f"We have reductate your {len(user)} score because you entered same word 3 times,your total score is {score} ")
print("Thank you for playing...")                            
                 