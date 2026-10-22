import random

num = random.randint(1, 100)
guess = 0
count = 1 
while guess != num :  
    guess = int(input("Your guess (1-100): "))
    if guess < num :
        print('Higher!')
        count += 1
    elif guess > num  :
        print('Lower!')
        count += 1
    elif guess == num :
        print(f"Correct! You need {count} attempts.")