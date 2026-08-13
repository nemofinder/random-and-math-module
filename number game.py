import random

playing = True

number = str(random.randint(10, 20))

print("I will generate a random number between 10 and 20 , and you have to guess one digit at a time. If you guess the correct digit, I will tell you that you are correct.")

print("The game ends when you get 1 hero1")

while playing:
    guess = input("Give me your best guess!! \n")

    if number == guess:
        print("You win")

        print("the number was ", number)
        break

    else :

        print("Your guess is incorrect. Try again! \n")