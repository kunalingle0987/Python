import random

num=random.randint(1,100)
a=-1
guesses=0

while(a!=num):
    guesses +=1
    a=int(input("Enter the number : "))
    if(a>num):
        print("Lower number please!")
    else:
        print("Higher number please..!")

print(f"Congratulations Buddy!.. You Guess a right Number {a } in {guesses} attempt.")
