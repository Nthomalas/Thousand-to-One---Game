#ADD PACKAGES
import random

#INTRODUCTION
print ("=== THOUSAND TO ONE ===")
print()
print("welcome to THOUSAND TO ONE: the number guessing game where YOU will be trying to guess the number selected from ZERO to ONE THOUSAND!")
print()

#INITIALIZATION
i = 1
number = random.randint(0,100)

#LOOP
while True:
    answer = int(input("What is your guess?:  "))
    if answer < number:
        print("Too low")
        i += 1
    elif answer > number:
        print("Too high" )
        i += 1
        continue
    elif  answer == number:
        print(f"\033[32m THAT ANSWER IS CORRECT! it only took you {i} guesses \033[0m")
        print()
        goAgain = input("Would you like to play again?:  ").strip().lower()
        if goAgain == "yes":
            number = random.randint(0,100)
            i = 1
            print("\033[31m New number chosen!\033[0m")
            print()
            continue
        else:
            print("Thank you for playing!")
            break
    
        
    

    
