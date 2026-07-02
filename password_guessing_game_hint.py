import random
#difine password list by difficulty 
easy_words =["apple","train","tiger","lala","tea"]
medium_words =["python","bottele","monkey","planet","laptop"]
hard_words=["elephant","diamond","umbrella","computer","mountain"]

print("wellcome to the password guessing game")
print("choose a difficulty level : easy, meduim or hard")
#2. user chooses difficulty
level=input('enter difficulty:').lower()
if level=="easy":
    secret =random.choice(easy_words)
elif level =="medium":
    secret =random.choice(medium_words)
elif level=="hard":
    secret =random.choice(hard_words)
else:    
    print("invalid choice.Defaulting to easy level")
    secret=random.choice(easy_words)

attemps =0
print("\nguess the secret password")
while True:
    guess=input("enter your guess:").lower()
    attemps +=1
    if guess ==secret :
        print(f"Congratulations! You gussed it in{attemps}attempts.")
        break

    hint=""  

    for i in range(len(secret)):
        if i<len(guess) and guess[i]==secret[i]:
            hint +=secret[i]
        else:
            hint +="_"
    print("Hint :"+hint)    
print("game over")    
